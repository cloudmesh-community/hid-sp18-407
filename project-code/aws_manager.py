from docopt import docopt
import boto3
from app import *

usage = """

Manage AWS Instance

Usage:
  aws_manager.py create_instances <amiID>
  aws_manager.py list_instances
  aws_manager.py stop_instances <stopinstanceID>
  aws_manager.py start_instances <startinstanceID>
"""

args = docopt(usage)

if args['create_instances']:
    amiID = args['<amiID>']
    create_instance(amiID)

elif args['list_instances']:
    list_instances()

elif args['stop_instances']:
    instanceID = args['<stopinstanceID>']
    stop_instances(instanceID)

elif args['start_instances']:
    instanceID = args['<startinstanceID>']
    start_instances(instanceID)

else:
    print(args)
