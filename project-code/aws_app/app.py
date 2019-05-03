import boto3
from docopt import docopt
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

## Create a new instance
def create_instances(amiID, key):
    response = ec2.create_instances(ImageId=amiID,
                                    KeyName=key,
                                    MinCount=1,
                                    MaxCount=1,
                                    InstanceType="t2.micro")
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
        print(instanceID," stopped")
    except ClientError as e:
        print(e)
        
#reboot instance:
def reboot_instance(instanceID):
    try:
        response = ec2.reboot_instances(InstanceIds=[instanceID], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print ('Error',e)

    print(instanceID," rebooted")

# start instances:
def start_instances(instanceID):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.start_instances(InstanceIds=instanceID, DryRun=False)
        print(response)
        print(instanceID, " Successfully started")
    except ClientError as e:
        print(e)
    
#get_dns:
def get_dns(instanceID):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_instances(InstanceIds=instanceID)
        print(response)
    except ClientError as e:
        print(e)

def aws_key_gen(keyname):
    ec2 = boto3.client('ec2')
    response = ec2.create_key_pair(KeyName=keyname)
    describe = ec2.describe_key_pairs()
    print(describe)
