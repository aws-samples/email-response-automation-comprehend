from os import environ
import boto3
from aws_cdk.core import CustomResource
import aws_cdk.core as core
import aws_cdk.aws_logs as logs
import aws_cdk.aws_iam as iam
import aws_cdk.custom_resources as cr
import aws_cdk.aws_lambda as lambda_
#import path as path

client = boto3.client('workmail', region_name='us-east-1')

class WorkMailOrgStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        orgname_param = core.CfnParameter(self, "OrganizationName",
                #type="String",
                default='my-sample-workmail-org'
                )

        username_param = core.CfnParameter(self, "UserName",
                #type="String",
                default='support'
                )
        pass_param = core.CfnParameter(self, "PassWord",
                #type="String",
                default='Welcome@123'
                )
        create_workmail_org_lambda = lambda_.Function(self, "WorkMailOrg",
                                                      runtime=lambda_.Runtime.PYTHON_3_6,
                                                      function_name='workmail_org_creation',
                                                      code=lambda_.Code.asset(
                                                          "workmailorg_project/Lambda"),
                                                      handler="workmailcreateorg.handler",
                                                      environment= {'work_org_name': orgname_param.value_as_string,
                                                                    'user_name': username_param.value_as_string,
                                                                    'password': pass_param.value_as_string}
                                                      )
                                                     
        
                
        create_workmail_org_lambda.role.attach_inline_policy(
            iam.Policy(
                self, "workmail_custom_resource_lambda_policy",
                policy_name = "workmail_custom_resource_lambda_policy",
                statements = [
                    iam.PolicyStatement(
                        actions = [
                            "workmail:*",
                            "ds:*",
                            "ses:*"
                        ],
                        resources= [ '*' ],
                    )
                ]
            )
        )


        is_complete_org = lambda_.Function(
                                            self, "workmail-org is complete",
                                            function_name="resource-is-complete-lambda",
                                            code=lambda_.Code.asset(
                                               "workmailorg_project/Lambda"),
                                            handler="workmailcreateorg.is_complete",
                                            runtime=lambda_.Runtime.PYTHON_3_6,
                                            environment= {'work_org_name':orgname_param.value_as_string,
                                                            'user_name': username_param.value_as_string,
                                                                'password': pass_param.value_as_string}
                                                                    )
                                            

        is_complete_org.role.attach_inline_policy(
            iam.Policy(
                self, "is_complete_custom_resource_lambda_policy",
                policy_name = "is_complete_custom_resource_lambda_policy",
                statements = [
                    iam.PolicyStatement(
                        actions = [
                            "workmail:*",
                            "ds:*",
                            "ses:*"
                        ],
                        resources= [ '*' ],
                    )
                ]
            )
        )

        create_workmail_org = cr.Provider(self, "workmail-org",
                                          on_event_handler=create_workmail_org_lambda,
                                          is_complete_handler=is_complete_org,  # optional async "waiter"
                                          log_retention=logs.RetentionDays.ONE_DAY#,  # default is INFINITE
                                          #role=my_role
                                          )

        CustomResource(self, id="WorkMailOrgResource",
                       service_token=create_workmail_org.service_token)
        