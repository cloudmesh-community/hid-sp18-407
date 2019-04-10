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

```python aws_manager.py create_instance <ami-image>```

There are currently 20 JuliaPro images listed on the Amazon EC2 community webpage.
One suitable image is ```ami-109cb475```, which includes JuliaPro 0.6.2.1_mkl on Ubuntu 16.04 64 bit server.  To search for alternate JuliaPro images, access <https://us-east-2.console.aws.amazon.com/ec2>. Select "Launch Instance" and then search for "JuliaPro" in the searchbar.  20 images will show up in the "Community" tab.  Select one of the image ids and add it to the command above where ```<ami-image>``` is your image id.  

## SSH into your EC2 instance
