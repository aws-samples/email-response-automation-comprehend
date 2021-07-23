import boto3


client = boto3.client('workmail',region_name='us-east-1')
workmail_domain_name = "vgs-sha-emailbot"

def handler(event, context):
  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  #if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception("Invalid request type: %s" % request_type)

def on_create(event):
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)
    # add your create code here...
    '''listresp = client.list_organizations()
    for i in listresp['OrganizationSummaries']:
        if i['State'] == "Active" and i['Alias'] == workmail_domain_name:
            OrgId=i['OrganizationId']
            print ('creating user')'''
    response = client.create_user(
                OrganizationId=OrgId,
                Name='Support',
                DisplayName='Bot Support',
                Password='Welcome@123'
            )
    physical_id = response['UserId']
    return { 'PhysicalResourceId': physical_id }
        else:
            print('failed to create the org')
    
    
def on_delete(event):
    physical_id = event["PhysicalResourceId"]
    print("delete resource %s" % physical_id)
    listresp = client.list_organizations()
    for i in listresp['OrganizationSummaries']:
        if i['State'] == "Active" and i['Alias'] == workmail_domain_name:
            OrgId=i['OrganizationId']
    response = client.delete_user(
            OrganizationId=OrgId,
            UserId=physical_id
    )
    response = {
     'PhysicalResourceId' : physical_id
     }
    return response
