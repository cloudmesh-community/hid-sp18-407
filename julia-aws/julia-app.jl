Pkg.add("AWSCore")
Pkg.add("Retry")
Pkg.add("SymDict")
#Pkg.add("AWSIAM")
Pkg.add("AWSSDK")
Pkg.add("AWSS3")

#using AWSEC2
using AWSS3
using AWSCore.Services

aws = AWSCore.Services.aws_config()
s3_create_bucket(aws, "myjuliabucket")
s3_enable_versioning(aws, "myjuliabucket")
s3_put(aws,"myjuliabucket", "key", "Hello!")

# cloudformation("CreateStack",
#               StackName = "AWSJuliaStack",
#               TemplateBody = read("template.yaml"),
#               #Parameters = [["InstanceType"   => "t2.micro"]],
#               Capabilities = ["CAPABILITY_IAM"])

#AWSS3.s3_list_buckets()
