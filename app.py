#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


from stacks.notebook_comprehend_train_deploy_project_stack import NotebookComprehendTrainDeployProjectStack
from stacks.workmailorg_project_stack import WorkMailOrgStack
from stacks.email_classification_workflow_stack import EmailClassificationWorkflowStack

app = core.App()

NotebookComprehendTrainDeployProjectStack(app, "comprehend-custom-classifier-dev-notebook-stack",env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))
WorkMailOrgStack(app, "workmail-organization-domain-user-dev-stack",env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))
EmailClassificationWorkflowStack(app, "email-class-workflow-stack",env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))


app.synth()
