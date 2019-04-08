import boto3
from docopt import docopt

doc = """Python Application

Usage:
  app.py [-start=INSTANCE] 
  app.py [-stop=INSTANCE] 
  app.py [-create=AMI] 
  app.py [-listinst]

Arguments:
  INSTANCE  existing instance
  AMI       amazon ami

Options:
"""

from docopt import docopt
ec2 = boto3.client('ec2')

## print("What would you like to do? Type 'create', 'start', 'stop', or 'reboot'")
## selection = input()

instance_id = input("name of the instance (format is i-<>) or similar:")
##List instance
def list_instances():
    response = ec2.describe_instances()
    print(response)

## Create a new EC2 instance:
def create_instance(ami_image_id):
    ec2.create_instances(ImageId=ami_image_id, MinCount=1, MaxCount=1, InstanceType='t2.micro')
    print("instance created:", ami_image_id)
    
## Start a previously-created instance
def start_instance(instance_id):
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print (response)
    except ClientError as e:
        print(e)

    print(instance_id," started")
    
# stop an Amazon instance:
def stop_instance(instance_id):
    try:
        response = ec2.stop_instance(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

    print(instance_id," stopped")
        
#reboot instance:
def reboot_instance(instance_id):
    try:
        response = ec2.reboot_instances(Instance_Ids=[instance_id], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print ('Error',e)

    print(instance_id," rebooted")

## if selection == 'create':
##    create_instance(ami_image_id)

##if selection == 'start':
##    start_instance(instance_id)

if __name__ == '__main__':
    main()
