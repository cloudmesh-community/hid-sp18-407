import boto3
from docopt import docopt

ec2 = boto3.resource('ec2')

## Create a new instance
def create_instances(amiID):
    response=ec2.create_instances(ImageId=amiID, MinCount=1, MaxCount=1, InstanceType="t2.micro")
    #response
    print (response)
    
create_instances('ami-109cb475')

## instance_id = input("name of the instance (format is i-<>) or similar:")
##List instance
def list_instances():
    response = ec2.describe_instances()
    print(response)

## Create a new EC2 instance:
#def create_instance(ami_image_id):
 #   ec2.create_instances(ImageId=ami_image_id, MinCount=1, MaxCount=1, InstanceType=t2.micro')
  #  print("instance created:", ami_image_id)
    

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

#if __name__ == '__main__':
   #main()
