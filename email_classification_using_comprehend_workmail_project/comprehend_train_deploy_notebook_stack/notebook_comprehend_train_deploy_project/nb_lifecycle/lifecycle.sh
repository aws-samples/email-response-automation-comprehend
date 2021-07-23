#!/bin/bash
set -e
nohup pip install --upgrade pip


cd /home/ec2-user/SageMaker

aws s3 cp s3://ee-assets-prod-us-east-1/modules/3d6fff6ad26244eeb40b0ea0c9651940/v1/comprehend_class_notebook.ipynb .