from docopt import docopt
import boto3
from app import *

usage = """

Manage AWS Instance

Usage:
  aws_manager.py create_instance <amiID>
  aws_manager.py list_instances 
"""

args = docopt(usage)

if args['create_instance']:
    amiId = args['amiID']
    create_instance(amiID)


elif args['list_instances']:
    list_instances()
