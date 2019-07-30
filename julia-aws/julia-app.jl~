import Pkg
Pkg.add("AWSCore")

using AWSS3

using AWSCore.Services

Services.cloudformation("CreateStack",
               StackName = "AWSJuliaStack",
               TemplateBody = read("template-test.yaml"),
               #Parameters = [["InstanceType"   => "t2.micro"]],
               Capabilities = ["CAPABILITY_IAM"])

