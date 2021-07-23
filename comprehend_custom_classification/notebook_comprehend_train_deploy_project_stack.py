from aws_cdk import core as cdk
import aws_cdk.aws_iam as iam
import aws_cdk.aws_sagemaker as sm
from aws_cdk import core
import base64

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

class NotebookComprehendTrainDeployProjectStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        nb_name_param = core.CfnParameter(self, "NotebookName",
                #type="String",
                default='notebook-instance-comprehend-training'
                )
        
        nb_config_name_param = core.CfnParameter(self, "NotebookConfigName",
                #type="String",
                default='notbook-lifecycle-load-notebook'
                )

        nb_config_role_name_param = core.CfnParameter(self, "RoleName",
                #type="String",
                default='sagemaker-notebook-execution-role'
                )

        #Role required for SageMaker to create the training job in Comprehend
        sm_exec_role = iam.Role(self, "sagemaker-notebook-execution-role",
                    role_name=nb_config_role_name_param.value_as_string,
                    description='Sagemaker execution policy for comprehend classification',
                    assumed_by=iam.CompositePrincipal(
                        iam.ServicePrincipal('sagemaker.amazonaws.com'),
                        iam.ServicePrincipal('comprehend.amazonaws.com')
                    ))

        #Policy for Sagemaker Full Access, fetching data from S3 bucket and run the classification training job

        sm_exec_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"))

        sm_exec_role.add_to_policy(iam.PolicyStatement(
            resources=["*"],
            actions=["s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket",
                "comprehend:CreateDocumentClassifier",
                "comprehend:DescribeDocumentClassifier",
                "comprehend:CreateEndpoint",
                "comprehend:TagResource",
                "comprehend:ClassifyDocument",
                "comprehend:DescribeEndpoint"]
        ))

        print(sm_exec_role)
        print("arn getting printed"+ sm_exec_role.role_arn)

        # required for comprehend to fetch the data from S3 bucket
        sm_exec_role.add_to_policy(iam.PolicyStatement(
                #resources=comp_exec_role.role_arn,
                resources=["*"],
                actions=["iam:GetRole",
                "iam:PassRole"]
            ))
        
        #Notebook lifecycle config

        #nb_lifecycle_config_name='notbook-lifecycle-load-notebook'

        LifecycleScriptStr = open("./comprehend_custom_classification/nb_lifecycle/lifecycle.sh", "r").read()

        content = [
            {"content": cdk.Fn.base64(LifecycleScriptStr)}
                    ]

        sagemaker_lifecycle= sm.CfnNotebookInstanceLifecycleConfig(self,'notebook life cycle config',
                                                notebook_instance_lifecycle_config_name=nb_config_name_param.value_as_string,
                                                on_create=content,
                                                on_start=content)
        
        
        #Notebook Creation
        sm.CfnNotebookInstance(self, 'notebook instance for comprehend training',
                                instance_type='ml.t2.xlarge', 
                                role_arn=sm_exec_role.role_arn,
                                notebook_instance_name=nb_name_param.value_as_string,
                                lifecycle_config_name=nb_config_name_param.value_as_string
                                )
