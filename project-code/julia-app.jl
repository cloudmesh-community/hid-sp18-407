using AWSIAM
using AWSCore

aws=AWSCore.aws_config()

iam(aws, "CreateUser",{"UserName" => "khickman"})
