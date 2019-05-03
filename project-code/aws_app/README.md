# Stochastic Modeling with Julia on AWS

This project seeks to implement AWS functionality in Python using boto3.  We create an EC2 instance and mount storage, install and interact with Jupyter notebook over Julia, download data, run models, and store the output to the volume.  

To implement: 

- Start with a clean working python environment, either pyenv or conda:

```mkdir julia_aws```

```cd julia_aws```

```git clone https://github.com/cloudmesh-community/hid-sp18-407.git```

```cd project-code```

```pip install -r requirements.txt```

If you haven't already, you'll need to configure your aws credentials using 
```aws configure``` 

Input your key, key id, default region (e.g. us-east-2), and output format (e.g. json). 

Now we can list existing EC2 instances, or create new ones and mount storage.  The default EC2 type for this project is t2.micro (free-tier eligible). Future implementations will allow for IAM policy creation, user creation, and IAM role assignments to users. 

## Create an EC2 instance

Using the following commands, create an EC2 instance of type t2.micro: 

```python aws_manager.py create_instance <ami-image> <keypairName>```

There are currently 20 JuliaPro images listed on the Amazon EC2 community webpage.
One suitable image is ```ami-109cb475```, which includes JuliaPro 0.6.2.1_mkl on Ubuntu 16.04 64 bit server.  To search for alternate JuliaPro images, access <https://us-east-2.console.aws.amazon.com/ec2>. Select "Launch Instance" and then search for "JuliaPro" in the searchbar.  20 images will show up in the "Community" tab.  Select one of the image ids and add it to the command above where ```<ami-image>``` is your image id.  

## SSH into your EC2 instance

To SSH into your EC2 instance, requires a 2048-bit RSA key, which can be
generated here. To generate the required RSA key pair to SSH into
your machine, issue the following command:

```python aws_manager.py aws_key_gen <keyname>```

Where keyname is an easily-remembered string like 'khickman_'

Next, obtain the Public DNS for the recently-started instance, use

```python aws_manager.py get_dns <instance_id>```

Now inbound (or ingress) SSH must be enabled on the machine to allow inbound SSH
traffic. Here we implement a simple, single access point. AWS does have many
options to expose the machine to outside requests, which can be found here
<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html>

Obtain your security group id's:

```aws ec2 describe-instance-attribute --instance-id i-0b8 e5e4abec4217b --attribute groupSet```

Use a group_id from above that has the correct permissions to access your EC2
instance:

```aws ec2 authorize-security-group-ingress --group-id <group_id> --protocol tcp --port 22 --cidr 0.0.0.0/0```

Now the EC2 instance is ready for SSH.  For the Amazon Linux AMI, the user name
is ```ubuntu```. Issue the following command to access the newly-created
instance where ```ec2-instance-name``` is the Public DNS name for the instance.
This can be obtained from the EC2 console or by issuing the
```describe_instances``` command. 

```ssh -i <path/to/pemfile.pem> <ubuntu@ec2-instance-name>```

The EC2 instance comes with Julia pre-downloaded. To run Julia, we must create a
symbolic link between a command and the executable file in the ```bin```
directory:

```sudo ln -s ~/JuliaPro-0.6.2.1/Julia/bin/julia /usr/local/bin/julia```

Before starting Julia, clone the repo containing the API files/services. 

```mkdir api_test```

```cd api_test```

```git clone <url here>.  

Now Julia is ready to be run on your machine, and you can issue the command: 

```julia```

to access the REPL.


Start the Genie App:
Issue a /download GET call
Issue a /train-test-split call

### Put this in the download function.  
data = CSV.read(download("https://archive.ics.uci.edu/ml/machine-learning-databases/00484/tripadvisor_review.csv"))