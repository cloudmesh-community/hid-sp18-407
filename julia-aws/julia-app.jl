#!/usr/bin/env julia0.6

#julia-app.jl

module AWSCoreModule

Pkg.add("AWSCore")
Pkg.add("DocOpt")
#Pkg.add("Retry")
#Pkg.add("SymDict")
#Pkg.add("AWSIAM")
#Pkg.add("AWSSDK")
#Pkg.add("AWSS3")

using AWSEC2
using AWSS3
using AWSCore
using DocOpt

#import 

export aws, create_s3, put_s3, list_buckets

aws = AWSCore.Services.aws_config()

function create_s3(bucket)
	create_bucket = s3_create_bucket(aws, bucket)
	create_bucket
	s3_enable_versioning(aws, bucket)	
	println(response)
end

function put_s3(bucket, object)
	put_object = s3_put(aws, bucket, object)
	put_object
	println(put_object)
end

function list_buckets()
	list_em = s3_list_buckets()	
	list_em
end
end

# cloudformation("CreateStack",
#               StackName = "AWSJuliaStack",
#               TemplateBody = read("template.yaml"),
#               #Parameters = [["InstanceType"   => "t2.micro"]],
#               Capabilities = ["CAPABILITY_IAM"])


