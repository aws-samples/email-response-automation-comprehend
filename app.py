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
from stacks.email_automation_workflow_stack import EmailAutomationWorkflowStack

app = core.App()

env = core.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"]
    )

NotebookComprehendTrainDeployProjectStack(app, "comprehend-custom-classifier-dev-notebook-stack", env=env)
WorkMailOrgStack(app, "workmail-organization-domain-user-dev-stack", env=env)
EmailAutomationWorkflowStack(app, "email-reponse-automation-workflow-stack", env=env)

app.synth()
