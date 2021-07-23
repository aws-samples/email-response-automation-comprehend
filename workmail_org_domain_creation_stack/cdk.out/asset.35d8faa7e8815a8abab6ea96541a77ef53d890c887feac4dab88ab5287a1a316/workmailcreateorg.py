import boto3
import os
from botocore.exceptions import ClientError


client = boto3.client('workmail',region_name='us-east-1')
workmail_domain_name = "vgs-sha-emailbot"

def handler(event, context):
  print(event)
  org_name = os.environ['work_org_name']
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event, org_name)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception("Invalid request type: %s" % request_type)

def on_create(event,orgName):
    
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)
    # call workmail organization api
    try:
        workmail_response = client.create_organization(
        Alias = orgName
        )
        print (workmail_response)
    except ClientError as q:
        print("Error while creating the organization: %s" % q)

    response = {'PhysicalResourceId' : workmail_response['OrganizationId']}
    return response


def on_update(event):
    physical_id = event["PhysicalResourceId"]
    props = event["ResourceProperties"]
    request_type = event["RequestType"]
    print("Nothing to do as an update event : update resource %s with props %s" %
        (physical_id, props))
    response = {
      'PhysicalResourceId': physical_id
    }
    return response

def on_delete(event):
    physical_id = event["PhysicalResourceId"]
    print("delete resource %s" % physical_id)

    user_avail = client.list_users(
                            OrganizationId=physical_id
                                            )
    for x in user_avail['Users']:
        print('start deleting users')
        if x['Name'] == 'support':
            try:
                response = client.deregister_from_work_mail(
                                OrganizationId=physical_id,
                                EntityId=x['Id']
                                )
                print(response)
                try:
                    response1 = client.delete_user(
                    OrganizationId=physical_id,
                    UserId=x['Id']
                    )
                    print(response1)
                    try:
                        response2 = client.delete_organization(
                                    OrganizationId=physical_id,
                                    DeleteDirectory=True
                                    )
                    except ClientError as m:
                        print("Error while deleting the organization: %s" % m)
                except ClientError as l:
                    print("Error while deleting the users: %s" % l)

            except ClientError as k:
                print("Error while deregistering the users: %s" % k)
            
    

# the workmail user creation and assign user to workmail domain has depndancies on below resources
# organization and domain - both should be in active state

def is_complete(event, context):
    physical_id = event["PhysicalResourceId"]
    request_type = event["RequestType"]

  # check if resource is stable based on request_type
    is_response = client.list_organizations()
    #print(is_response)
    is_ready = False
    for i in is_response['OrganizationSummaries']:
        #checking the status of the organization created
        if i['State'] == "Active" and i['Alias'] == "vgs-sha-emailbot":
            print ('user getting created.....')
            #if yes creating the user and registering the user is done. if not goes to exception block
            try:
                user_response = client.create_user(
                                    OrganizationId=i['OrganizationId'],
                                    Name='support',
                                    DisplayName='Bot Supprt',
                                    Password='Welcome@123')
                response = client.register_to_work_mail(
                                    OrganizationId=i['OrganizationId'],
                                    EntityId=user_response['UserId'],
                                    Email='support@vgs-sha-emailbot.awsapps.com')
                is_ready = True
            except ClientError as e:
                print(e.response)
                # if the error is NameAvailabilityException, it will go for user registeration for email
                if e.response['Error']['Code'] == 'NameAvailabilityException':
                    print("User already exists..registering user to the domain")
                    try:
                        user_avail = client.list_users(
                                            OrganizationId=i['OrganizationId']
                                            )
                        for x in user_avail['Users']:
                            print('start registering users')
                            if x['Name'] == 'support':
                                print(x['Id'])
                                try:    
                                    reg_response = client.register_to_work_mail(
                                                OrganizationId=i['OrganizationId'],
                                                EntityId=x['Id'],
                                                Email='support@vgs-sha-emailbot.awsapps.com')
                                    is_ready = True
                                    print (reg_response)
                                except ClientError as g:
                                    print(g.response)
                                    if g.response['Error']['Code'] == 'MailDomainStateException':
                                        print('Domain is still getting created..please wait')
                                        is_ready = False
                                    else:                                       
                                        print("Unexpected error: %s" % g) 
                                        is_ready = True 
                    except ClientError as f:
                        print(f.response)
                        # if the error is NameAvailabilityException (means user already exist) and should go to user registration
                        if f.response['Error']['Code'] == 'NameAvailabilityException':
                            is_ready = False
                            print ('Domain is still getting created..please wait')
                        else:
                            print("Unexpected error on lissting users: %s" % f)
                            is_ready = True
                elif e.response['Error']['Code'] == 'MailDomainStateException':
                    print('Domain is still getting created..please wait')
                    is_ready = False
                else:
                    print("Unexpected error: %s" % e)     
                    is_ready = True
    return { 'IsComplete': is_ready }
