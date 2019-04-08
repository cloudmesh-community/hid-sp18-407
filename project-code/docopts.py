"""
Usage:
  app.py [-start=INSTANCE] 
  app.py [-stop=INSTANCE] 
  app.py [-create=AMI] 
  app.py [-listinst]

Arguments:
  INSTANCE  existing instance
  AMI       amazon ami

Options:
  -
  --stop
  --create

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0rc2')
print(arguments)
