import boto3
from docopt import docopt
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

## Create a new instance
def create_instances(amiID):
    response = ec2.create_instances(ImageId=amiID, MinCount=1, MaxCount=1, InstanceType="t2.micro")
    response
    print(response)
    
##List instance
def list_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)

# stop an EC2 instance:
def stop_instances(instanceID):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.stop_instances(InstanceIds=[instanceID], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
    print(instanceID," stopped")
        
#reboot instance:
def reboot_instance(amiID):
    try:
        response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print ('Error',e)

    print(instance_id," rebooted")

# start instances:
def start_instances(instanceID):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.start_instances(InstanceIds=instanceID, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
    print(instanceID, " Successfully started")
