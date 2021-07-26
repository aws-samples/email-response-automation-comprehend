# Email Classification Using Amazon Comprehend project!

This project is developed to showcase how Amazon comprehend can be used to classify the incoming email and respond back to the customer automatically. 

Supporting customer via email channel is one of the big task for every organization sinch it involves human resources, space, devices,and other technologies. Also, this very expensive process and not addressing customer queries leads to huge customer churnout and impacting the revenue and reputation of the organization. 

Many of a times, customer asks the basic questions and it is unnecessary that customer care rep to respond to all the emails unless the request is critical or sensitive. Amazon Comprehend is managed AI service which helps to extract insights from the content of documents. In this project, we used Amazon Workmail to receive the customer email and that triggers the lambda function to pass the content to Amazon Comprehend to classify content and respond back to the customer via email with pre-defined answer for the known requests.

## Process Flow / Architecture Diagram

![Automated_Email_Response_using_Amazon_Comprehend](/uploads/e7cdbe48f2e56b46086d962d04887d62/Automated_Email_Response_using_Amazon_Comprehend.jpg)

## CDK project structure :
The soultion comprised of two cdk stacks.

comprehend-custom-classifier-dev-notebook-stack : Creates the Amazon sagemaker jupyter notbook instance pre-loaded with .ipynb notbook and creates IAM role required for executing comprehend custom classification training, deployment, and S3 data access.
workmail-organization-domain-user-dev-stack : Creates the Amazon workmail with domain, user, inbox access.

## Pre-requisites
- An AWS Account with region us-east-1
- Make sure servics mentioned in the architecturea and its service limits in region us-east-1 and your account
- AWS CLI and AWS CDK installed installed and configured with Access Key ID and Secret Access Key with access to AWS CloudFormation to create resources in your AWS account
- Python3-pip installed in you terminal or any IDK 

## Steps to deploy the project
1. Clone the repository.

2. This project is set up like a standard Python project. To create the virtualenv it assumes that there is a python3 (or python for Windows) executable in your path with access to the venv package. create the virtualenv using following command.
```
$ python3 -m venv .venv 
```

3. Use the following step to activate your virtualenv.
```
$ source .venv/bin/activate
```
If you are a Windows platform, you would activate the virtualenv like this:
```
% .venv\Scripts\activate.bat
```
Once the virtualenv is activated, you can install the required dependencies.
```
$ pip install -r requirements.txt
```
4. Deploying the solution :

Deploying new Sagemaker Notebook Instance with IAM Roles and pre-loaded .ipynb notebook : Execute following command by passing optional paramaters
```
cdk deploy comprehend-custom-classifier-dev-notebook-stack  --parameters NotebookName=<Notebook Name> --parameters NotebookConfigName=<Notebook Config Name> --parameters RoleName=<SageMaker execution role name>
```

Deploying new Workmail domain, user, user registration and inbox: Execute following command by passing optional paramaters
```
cdk deploy workmail-organization-domain-user-dev-stack --parameters OrganizationName=<Organization Name> --parameters UserName=<Support Username> --parameters PassWord=<Password>
```
Note : Please note that these both deployments approximately 20 to 25 minutes

After the stacks are succefully deployed (You can see if there is an error as the cdk output otherwise it says stacks creation succeful.), please open the .ipynb notebook and execute all the scripts in the notebook in sequence. The last script in the notebook will deploy the model and gives you the ARN of the deployed resource. Please use this ARN as the parameter for the next stack deployment.

Deploying AWS Lammbda fucntions, Amazon dynamoDB and SNS notifications: Execute the following command 
```
CDK deploy <Shamica CDK stack>
```

Setting up the Inbound rules in Amazon Workmail using the lambda function generated in previous stack. Please use the  'Amazon Workmail Inbound Rule Setup with Lambda.docx' file to complete this setup


## Testing the solution
