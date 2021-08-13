from aws_cdk import (
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_dynamodb as dynamodb,
    aws_ses as ses,
    core
)

import os.path as path
import json

class EmailClassificationWorkflowStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        human_topic = self.human_workflow_topic()

        classification_lambda = self.classify_email_lambda(human_topic)
        
        workmail_lambda = self.workmail_integration_lambda(classification_lambda)
        
        self.register_email_temapltes()
        
        #email_templates_dynamodb = self.email_templates_dynamodb() 
        
    
    def workmail_integration_lambda(self, classification_lambda):
        
        # workmail_arn = self.node.try_get_context("workmail_arn")
        # if not workmail_arn:
        #      raise ValueError("Please provide arn of the workmail domain. You can provide that by specifying workmail_arn context variable")
        
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
        
        email_classification_endpoint_arn = self.node.try_get_context("email_classification_endpoint_arn")
        if not email_classification_endpoint_arn:
             raise ValueError("Please provide email classification endpoint. You can provide that by specifying email_classification_endpoint_arn context variable")

        support_email = self.node.try_get_context("support_email")
        if not support_email:
             raise ValueError("Please provide email of the support team. You can provide that by specifying support_email context variable")
        
        email_classify_lambda = lambda_.Function(
            self, "id_classify_emails_lambda_fn", 
            function_name="classify-emails-lambda-fn",
            code = lambda_.Code.from_asset(path.join("./lambda", "classify-emails-lambda")),
            handler = "lambda_function.lambda_handler",
            runtime = lambda_.Runtime.PYTHON_3_8,
            timeout = core.Duration.minutes(1),
            environment={
                "EMAIL_CLASSIFICATION_ENDPOINT_ARN" : email_classification_endpoint_arn,
                "HUMAN_WORKFLOW_SNS_TOPIC_ARN" : human_workflow_topic.topic_arn,
                "SOURCE_EMAIL" : support_email
            }
        )
        
        email_classify_lambda.add_to_role_policy(
            iam.PolicyStatement(
                        actions = [
                            "comprehend:*",
                        ],
                        resources= [ email_classification_endpoint_arn ]
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
        
        human_workflow_email = self.node.try_get_context("human_workflow_email")
       
        if not human_workflow_email:
             raise ValueError("Please provide email to forward the human workflow events. You can provide that by specifying human_workflow_email context variable")
             
        topic =  sns.Topic(
            self, "id_human_workflow_topic",
            display_name="Email-classification-human-workflow-topic",
            topic_name="Email-classification-human-workflow-topic"
        )
        
        topic.add_subscription(subs.EmailSubscription(human_workflow_email))
        
        return topic
        
    def email_templates_dynamodb(self):
        return dynamodb.Table(
            self, "id_email_templates_db",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
        )
        
        
    def register_email_temapltes(self):
        
        f = open('./stacks/email_templates.json',)
        data = json.load(f)
        for template in data['templates']:
            ses.CfnTemplate(
                self, "id_ses_template_{}".format(template['template_name']),
                template= ses.CfnTemplate.TemplateProperty(**template)
            )
        f.close()