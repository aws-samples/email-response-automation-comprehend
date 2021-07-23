# Email Classification Using Amazon Comprehend

This project is developed to showcase how Amazon comprehend can be used to classify the incoming email and respond back to the customer automatically. 

Supporting customer via email channel is one of the big task for every organization sinch it involves human resources, space, devices,and other technologies. Also, this very expensive process and not addressing customer queries leads to huge customer churnout and impacting the revenue and reputation of the organization. 

Many of a times, customer asks the basic questions and it is unnecessary that customer care rep to respond to all the emails unless the request is critical or sensitive. Amazon Comprehend is managed AI service which helps to extract insights from the content of documents. In this project, we used Amazon Workmail to receive the customer email and that triggers the lambda function to pass the content to Amazon Comprehend to classify content and respond back to the customer via email with pre-defined answer for the known requests.

## Process Flow / Architecture Diagram

![Automated_Email_Response_using_Amazon_Comprehend](/uploads/464041959b84ee1c9b5ee56a18e2b164/Automated_Email_Response_using_Amazon_Comprehend.jpg)

## Pre-requisites
- An AWS Account with region us-east-1
- Make sure servics mentioned in the architecturea and its service limits in region us-east-1 and your account
- AWS CLI and AWS CDK installed installed and configured with Access Key ID and Secret Access Key to create the resources in your AWS account
- Python3-pip installed in you terminal or IDK

## Services used in this project
- Amazon Comprehend - For Email Classification
- Amazon Workamil - For Email Domain, Support user Email Alias and Inbox Creation
- DynamoDB - For storing, and retrieiving email templates and transaction status
- SES/SNS - For Email response back to customer email
- Lambda - For triggering the event upon receiving the email and response callout
- Sagemaker Notebook - For Custom Classification Training and Deployment
- CDK - For infrstrucutre deployment

## List of steps required to complete this project
1. Donwload and deploy the CDK using the repository notebook_comprehend_train_deploy_project. This will create the notbook instnce with pre-loaded .ipynb notebook file with IAM role required to execute the trining and deployment
2. Execute the .ipynb file from notebook instance. This will execute the custom classification training and deployment in Amazon Comprehend
3. Download and deploy the CDK using the repository comprehend_email_classification_project. This will create the Amazon WorkMail organization, domain, users, and user registration to the domain. When csutomer sends the email, you will see the message in inbox of this support user.
4. Download and deploy the CDK using repository xxxxxxxxxxxxx. This will create the Dynamo DB table,SES, and Lambda functions required to store the email template and send the email back to customer with response.
5. Adding Lambda function in Workmail Organization inbound rules to invoke the lambda function whenever user sends an email.

## Tutorial
### Step1: Deploying SageMaker Notebook resource

Check whether CDK is installed in your terminal
<clipboard-copy>

CDK --version </code>
</clipboard-copy>


### Step2: Comprehend Customer Classification Training and Deployment with sample data
### Step3: Deploying Amazon WorkMail organization, domain, Inbox and users
### Step4: Deploying AWS Lambda, Amazon DynamoDB, Amazon Simple Notification Service 
### Step5: Configuring inbound rules with Lambda function

##Testing the solution
