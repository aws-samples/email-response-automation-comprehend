# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import email
import os
import logging
import email

logger = logging.getLogger()
logger.setLevel(logging.INFO)

workmail = boto3.client('workmailmessageflow')
classification_lambda = boto3.client('lambda')

classification_lambda_function_name = os.getenv("EMAIL_CLASSIFICATION_LAMBDA_FN_NAME")

if not classification_lambda_function_name:
   raise ValueError("EMAIL_CLASSIFICATION_LAMBDA_FN_NAME env variable required.")
   
def start_classification_flow():
   
   event = {
     "email" : {
      "body": "Todays weather is rainy.",   
      "subject": "Howdy",
      "to" : "amilaaina@gmail.com"
     },
     "meta" : {
         "source" : "workmail",
         "id" : "adasdsadasdasdas"
     }
   }
   
   classification_lambda.invoke(
      FunctionName=classification_lambda_function_name
   )

def lambda_handler(event, context):
    
    msg_id = event['messageId']
    logger.info("An Email received with messageId : [{}]".format(msg_id))
    
    raw_msg = workmail.get_raw_message_content(messageId=msg_id)

    parsed_email = email.message_from_bytes(raw_msg['messageContent'].read())
    logger.info("Email content is : {}".format(parsed_email))
    
    text_content = parsed_email.get_payload(decode=True)
    text_charset = parsed_email.get_content_charset()

    if text_content and text_charset:
         email_text =  text_content.decode(text_charset)
         logger.info("Content of the email is : [{}]".format(email_text)) 
         start_classification_flow()
         
         
    else:
       raise ValueError()


       