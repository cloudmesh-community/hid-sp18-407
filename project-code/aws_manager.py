from docopt import docopt
import boto3
from app import *

usage = """

Manage AWS Instance

Usage:
  aws_manager.py create_instance <amiID>
"""

args = docopt(usage)

if args['create_instance']:
    amiId = args['amiID']
    create_instance(amiID)
