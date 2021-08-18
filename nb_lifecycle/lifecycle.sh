#!/bin/bash
set -e

nohup pip install --upgrade pip

cd /home/ec2-user/SageMaker

aws s3 cp s3://S3URL/comprehend_class_entity_train_deploy_notebook.ipynb .