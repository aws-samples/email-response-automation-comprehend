from aws_cdk import (
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_ses as ses,
    core
)

import os.path as path
import json

class EmailAutomationWorkflowStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        human_topic = self.human_workflow_topic()

        classification_lambda = self.classify_email_lambda(human_topic)
        
        workmail_lambda = self.workmail_integration_lambda(classification_lambda)
        
        self.register_email_temapltes()
        
    
    def workmail_integration_lambda(self, classification_lambda):
        
        workmail_lambda = lambda_.Function(
            self, "id_workmail_integration_lambda_lambda_fn", 
            function_name="workmail-integration-lambda-fn",
            code = lambda_.Code.from_asset(path.join("./lambda", "workmail-integration-lambda")),
            handler = "lambda_function.lambda_handler",
            runtime = lambda_.Runtime.PYTHON_3_8,
            timeout = core.Duration.minutes(1),
            environment={
                "EMAIL_CLASSIFICATION_LAMBDA_FN_NAME" : classification_lambda.function_name
            }
        )
        
        current_region = self.region
        
        principal = iam.ServicePrincipal("workmail.us-west-2.amazonaws.com")
        
        workmail_lambda.grant_invoke(principal)
        
        workmail_lambda.add_to_role_policy(
            iam.PolicyStatement(
                        actions = [
                            "workmailmessageflow:GetRawMessageContent",
                        ],
                        resources= [ '*' ]
                    )
            
        )
        
        classification_lambda.grant_invoke(workmail_lambda)
        
        return workmail_lambda
        
        
    def classify_email_lambda(self, human_workflow_topic):
        
        email_classification_endpoint_arn = core.CfnParameter(self, "emailClassificationEndpointArn",
                #type="String"
                ).value_as_string
                
        email_entity_recognition_endpoint_arn = core.CfnParameter(self, "emailEntityRecognitionEndpointArn",
                #type="String"
                ).value_as_string
                
        support_email = core.CfnParameter(self, "supportEmail",
                #type="String"
                ).value_as_string
        
        email_classify_lambda = lambda_.Function(
            self, "id_classify_emails_lambda_fn", 
            function_name="classify-emails-lambda-fn",
            code = lambda_.Code.from_asset(path.join("./lambda", "classify-emails-lambda")),
            handler = "lambda_function.lambda_handler",
            runtime = lambda_.Runtime.PYTHON_3_8,
            timeout = core.Duration.minutes(1),
            environment={
                "EMAIL_CLASSIFICATION_ENDPOINT_ARN" : email_classification_endpoint_arn,
                "EMAIL_ENTITY_RECOGNITION_ENDPOINT_ARN" : email_entity_recognition_endpoint_arn,
                "HUMAN_WORKFLOW_SNS_TOPIC_ARN" : human_workflow_topic.topic_arn,
                "SOURCE_EMAIL" : support_email
            }
        )
        
        email_classify_lambda.add_to_role_policy(
            iam.PolicyStatement(
                        actions = [
                            "comprehend:*",
                        ],
                        resources= [ email_classification_endpoint_arn, email_entity_recognition_endpoint_arn ]
                    )
            
        )

        email_classify_lambda.add_to_role_policy(
            iam.PolicyStatement(
                        actions = [
                            "ses:SendTemplatedEmail",
                        ],
                        resources= [ '*' ]
                    )
            
        )
        
        human_workflow_topic.grant_publish(email_classify_lambda)
        
        return email_classify_lambda
        
            
    def human_workflow_topic(self):
        
        human_workflow_email = core.CfnParameter(self, "humanWorkflowEmail",
                #type="String"
                ).value_as_string
             
        topic =  sns.Topic(
            self, "id_human_workflow_topic",
            display_name="Email-classification-human-workflow-topic",
            topic_name="Email-classification-human-workflow-topic"
        )
        
        topic.add_subscription(subs.EmailSubscription(human_workflow_email))
        
        return topic
        
        
    def register_email_temapltes(self):
        
        f = open('./sample_data/email_templates.json',)
        data = json.load(f)
        for template in data['templates']:
            ses.CfnTemplate(
                self, "id_ses_template_{}".format(template['template_name']),
                template= ses.CfnTemplate.TemplateProperty(**template)
            )
        f.close()