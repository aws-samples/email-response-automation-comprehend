import boto3


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
    response = client.delete_organization(
        OrganizationId=physical_id,
        DeleteDirectory=True
    )

def is_complete(event, context):
    physical_id = event["PhysicalResourceId"]
    request_type = event["RequestType"]

  # check if resource is stable based on request_type
    response = client.describe_organization(OrganizationId='PhysicalResourceId')
    is_ready = False
    if response['State'] == "Active":
        print ('user getting created.....')
        user_response = client.create_user(
                                OrganizationId=response['OrganizationId']
                                Name='support',
                                DisplayName='Bot Supprt',
                                Password='Welcome@123')
        is_ready = True
    return { 'IsComplete': is_ready }
