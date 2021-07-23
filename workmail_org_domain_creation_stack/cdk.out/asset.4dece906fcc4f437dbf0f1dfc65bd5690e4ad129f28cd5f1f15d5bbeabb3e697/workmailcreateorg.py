import boto3
from botocore.exceptions import ClientError


client = boto3.client('workmail',region_name='us-east-1')
workmail_domain_name = "vgs-sha-emailbot"

def handler(event, context):
  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception("Invalid request type: %s" % request_type)

def on_create(event):
    
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)
    # call workmail organization api
    workmail_response = client.create_organization(
    Alias=workmail_domain_name,
    )
    print (workmail_response)

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
            response1 = client.delete_user(
                    OrganizationId=physical_id,
                    UserId=x['Id']
                    )
    response2 = client.delete_organization(
        OrganizationId=physical_id,
        DeleteDirectory=True
    )

def is_complete(event, context):
    physical_id = event["PhysicalResourceId"]
    request_type = event["RequestType"]

  # check if resource is stable based on request_type
    is_response = client.list_organizations()
    #print(is_response)
    is_ready = False
    for i in is_response['OrganizationSummaries']:
        if i['State'] == "Active" and i['Alias'] == "vgs-sha-emailbot":
            print ('user getting created.....')
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
                if e.response['Error']['Code'] == 'NameAvailabilityException':
                    print("User already exists..registering user to the domainX")
                    try:
                        user_avail = client.list_users(
                                            OrganizationId=i['OrganizationId'],
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
                    except ClientError as f:
                        print(f.response)
                        if f.response['Error']['Code'] == 'MailDomainStateException':
                            is_ready = False
                            print ('Domain is still getting created..please wait')
                        else:
                            print("Unexpected error on lissting users: %s" % f)
                elif e.response['Error']['Code'] == 'MailDomainStateException':
                    print('Domain is still getting created..please wait')
                    is_ready = False
                else:
                    print("Unexpected error: %s" % e)     
    return { 'IsComplete': is_ready }
