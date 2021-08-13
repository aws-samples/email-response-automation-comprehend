# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import logging
import os
import json 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

comprehend_client = boto3.client('comprehend')
sns_client = boto3.resource('sns')
ses_client = boto3.client('ses')


endpoint_name = os.getenv("EMAIL_CLASSIFICATION_ENDPOINT_ARN")
threashold = os.getenv("EMAIL_CLASSIFICATION_THREASHOLD")
human_workflow_topic_arn = os.getenv("HUMAN_WORKFLOW_SNS_TOPIC_ARN")
source_email = os.getenv("SOURCE_EMAIL")


if not endpoint_name:
   raise ValueError("env variable EMAIL_CLASSIFICATION_ENDPOINT_ARN is required.")
   
if not human_workflow_topic_arn:
   raise ValueError("env variable HUMAN_WORKFLOW_SNS_TOPIC is required.")  
   
if not source_email:
   raise ValueError("env variable SOURCE_EMAIL is required.")      
   
if not threashold:
   threashold = 0.6
   
human_workflow_topic = sns_client.Topic(human_workflow_topic_arn)

def call_endpoint(email_body):
   
   response = comprehend_client.classify_document(
    Text=email_body,
    EndpointArn=endpoint_name
   )
   
   return response
   
   
def best_class(results):
   return max(results['Classes'], key=lambda x : x['Score'])
   
   
def is_good_enough(best_result):
   return best_result['Score'] >= threashold
   
def send_user_email(email, template_name):
   logger.info("Sending email to the user : [{}]".format(email))
   response = ses_client.send_templated_email(
     Source=source_email,
     Destination={
       'ToAddresses': [
         email['to'],
       ]
     },
     Template=template_name,
     TemplateData='{ }'
   )
   

def send_to_human_workflow_topic(email):
   
   human_workflow_topic.publish(
      Message = json.dumps(email, indent = 4)  ,
      Subject = "Human workflow entry found"
   )
   
def validate_params(event):
   
   email = event['email']
   meta = event['meta']
   
   if not email :
      raise ValueError("No email found to classify.")
   if not meta :
      raise ValueError("No metadata found.")
   
   email_body = email['body']
   email_subject = email['subject']
   user_email = email['to']
   message_source = meta['source']
   message_id = meta['id']
   
   
   if not email_body:
      raise ValueError("No email body found to classify.")
   if not email_subject:
      raise ValueError("No email subject found.")
   if not user_email:
      raise ValueError("No user email found.")
   if not message_source:
      raise ValueError("No email source found.")
   if not message_id:
      raise ValueError("No email source id found.")
      
   return email, meta

def lambda_handler(event, context):
 
   email, meta = validate_params(event)   
   
   logger.info("Executing the email classification lambda function with email content {}".format(email['body']))
   
   results = call_endpoint(email['body'])
   
   logger.info("Classification results returned. {}".format(results))
   
   best_intent = best_class(results)
   
   if(is_good_enough(best_intent)):
      logger.info("Classification passed the threashold. Best matched intent is [{}]".format(best_intent['Name']))
      send_user_email(event['email'], best_intent['Name'])
   else:
      send_to_human_workflow_topic(event['email'])
      
   return best_intent
  
       