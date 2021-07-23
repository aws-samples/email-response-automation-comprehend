#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from comprehend_train_deploy_notebook_stack.notebook_comprehend_train_deploy_project_stack import NotebookComprehendTrainDeployProjectStack
#from EmailbotProjectStack.EmailbotProjectStack import EmailbotProjectStack

app = core.App()
NotebookComprehendTrainDeployProjectStack(app, "comprehend-custome-classifier-dev-notebook-stack")

app.synth()
