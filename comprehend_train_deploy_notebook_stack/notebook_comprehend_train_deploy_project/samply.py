from aws_cdk import core as cdk
import base64
LifecycleScriptStr = open("./notebook_comprehend_train_deploy_project/nb_lifecycle/lifecycle.sh", "r").read()

content = [
            {"content": cdk.Fn.base64(LifecycleScriptStr)}
                    ]


print(LifecycleScriptStr) 
print(content)