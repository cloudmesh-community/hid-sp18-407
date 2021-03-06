# Data Management with Julia and AWS

This project seeks to implement AWS functionality in Python using boto3.  We create an EC2 instance and mount storage, install and interact with Jupyter notebook over Julia, download data, run models, and store the output to the volume.  

To implement: 

- Start with a clean working python environment, either pyenv or conda:

```mkdir julia_aws```

```cd julia_aws```

```git clone https://github.com/keithhickman08/aws_app.git```

```cd aws_app```

Or, if cloning from cloudmesh-community: 

```git clone https://github.com/cloudmesh-community/hid-sp18-407.git```

```cd project-code```

Then, regardless of source:

```pip install -r requirements.txt```

If you haven't already, you'll need to configure your AWS credentials using the .pem files provided when your credentials were created.  AWS will look for those in the /.aws directory.   

Now we can list existing EC2 instances, or create new ones and mount storage.  The default EC2 type for this project is t2.micro (free-tier eligible). Future implementations will allow for IAM policy creation, user creation, and IAM role assignments to users. 

## Create an EC2 instance

Before typing the first command, locate the key-pair you wish to use by issuing: 

```aws ec2 describe-key-pairs```

Using the following commands, create an EC2 instance of type t2.micro: 

```python aws_manager.py create_instance <ami-image> <keypairName>```

There are currently 20 JuliaPro images listed on the Amazon EC2 community webpage.
One suitable image is ```ami-109cb475```, which includes JuliaPro 0.6.2.1_mkl on Ubuntu 16.04 64 bit server.  To search for alternate JuliaPro images, access <https://us-east-2.console.aws.amazon.com/ec2>. Select "Launch Instance" and then search for "JuliaPro" in the searchbar.  20 images will show up in the "Community" tab.  Select one of the image ids and add it to the command above where ```<ami-image>``` is your image id.  

## Start your EC2 instance

```python aws_manager.py start_instances <instance_id>``` with no quotes or string literals. 

## SSH into your EC2 instance

To SSH into your EC2 instance, requires a 2048-bit RSA key, which can be
generated here. To generate the required RSA key pair to SSH into
your machine, issue the following command:

```python aws_manager.py aws_key_gen <keyname>```

Where keyname is an easily-remembered string like 'khickman_'

Next, obtain the Public DNS for the recently-started instance, use

```python aws_manager.py get_dns <instance_id>```

The Public DNS name may take a few moments to populate. 

Now inbound (or ingress) SSH must be enabled on the machine to allow inbound SSH
traffic. Here we implement a simple, single access point. AWS does have many
options to expose the machine to outside requests, which can be found here
<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html>

Now the EC2 instance is ready for SSH.  For the Amazon Linux AMI, the user name
is ```ubuntu```. Issue the following command to access the newly-created
instance where ```ec2-instance-name``` is the Public DNS name for the instance.
This can be obtained from the EC2 console or by issuing the
```describe_instances``` command. 

```ssh -i <path/to/pemfile.pem> <ubuntu@ec2-public-dns>```

The first time SSH'ing into a instance, users will receive the following warning: 

```The authenticity of host '<ip-address>.us-east-2.compute.amazonaws.com' can't be established. ECDSA key fingerprint is <fingerprint-id>.  Are you sure you want to continue connecting (yes/no)?```

Type yes and proceed. 

If SSH does not work, attempt the following steps. 

1) Obtain your security group id's:

```aws ec2 describe-instance-attribute --instance-id i-0b8 e5e4abec4217b --attribute groupSet```

2) Use a group_id from above that has the correct permissions to access your EC2
instance:

```aws ec2 authorize-security-group-ingress --group-id <group_id> --protocol tcp --port 22 --cidr 0.0.0.0/0```


## Julia Setup on EC2

Due to an package manager issue with the pre-installed Julia distribution (0.6.2), it is recommended to use an official Julia Docker image. 

### Install Julia 1.0.1 on EC2 Instance: 

```bash
$ sudo apt update
$ sudo apt -y install build-essential
## Create a REST API Service in Julia
```

### Download and Extract Julia, then create symbolic link to Julia executable:

```
$ wget https://julialang-s3.julialang.org/bin/linux/x64/1.0/julia-1.0.1-linux-x86_64.tar.gz
$ tar xvfz julia-1.0.1-linux-x86_64.tar.gz
$ sudo ln -s /home/ubuntu/julia-1.0.1/bin/julia /usr/local/bin/julia
```

Now Julia will run using the symbolic link created in the last line of code by issuing ```julia``` in bash. 

### Implement REST Service

Implementing a REST API service on your AWS instance is simple using the Genie package.  <https://github.com/essenciary/Genie.jl>

Julia must be in the App's home directory. You can check this in Julia by typing ```pwd()``` to print the working directory.  

Bring Genie into scope and load the app: 

```
julia> using Genie
julia> Genie.loadapp()
```

Now the app is active in the environment and is ready to be started with ```Genie.startapp()```.  
Note the URLs given in the shell prompt; possibly something like http://127.0.0.1:8000.  Open a browser and paste or type that URL into the address bar, and you should see a Genie Welcome page.  

To download your data, add in "/getdata" to the end of the url to access the data endpoint. Calling this endpoint will download a datafile consisting of user reviews of various travel, restaurant, and entertainment venues.  Further development of this endpoint will allow users to specify datafile paths, handle different types of data, etc... 

Now we can prepare the data for a machine learning model in our AWS instance by shuffling and training, testing, and splitting the model.  Included in the git repo JuliaData is a julia script that will access the recently downloaded data and split it into train and test sets. To access this script, ```^c``` (control-c) out of the Julia App, and make sure that the ```julia>``` prompt is visible.  

To run a Julia script, type 
```julia
julia> include("traintest.jl")
```

Now all of the data plus easy to read train and test files are ready for ML processing! 
