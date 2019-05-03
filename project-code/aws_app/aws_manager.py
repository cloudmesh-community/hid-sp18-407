from docopt import docopt
import boto3
from app import *

usage = """

Manage AWS Instance

Usage:
  aws_manager.py create_instances <amiID> <keypairName>
  aws_manager.py list_instances
  aws_manager.py stop_instances <stopinstanceID>
  aws_manager.py start_instances <startinstanceID>
  aws_manager.py get_dns <instanceID>
  aws_manager.py key_gen <keyname>
"""

args = docopt(usage)

if args['create_instances']:
    amiID = args['<amiID>']
    key = args['<keypairName>']
    create_instances(amiID, key)

elif args['list_instances']:
    list_instances()

elif args['stop_instances']:
    instanceID = args['<stopinstanceID>']
    stop_instances(instanceID)

elif args['start_instances']:
    instanceID = (args['<startinstanceID>'],)
    start_instances(instanceID)

elif args['get_dns']:
    instanceID = (args['<instanceID>'],)
    get_dns(instanceID)

elif args['key_gen']:
    keyname = args['<keyname>']
    aws_key_gen(keyname)

else:
    print(args)
