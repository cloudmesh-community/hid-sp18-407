Pkg.add("AWSCore")
Pkg.add("DocOpt")

include("julia-app.jl")

using AWSCoreModule
using DocOpt

const doc = """AWScore module

Usage:
	julia-manager.jl create_s3 <bucket.name>
	julia-manager.jl delete_s3 <bucket.name>
	julia-manager.jl put_s3 <object>
	julia-manager.jl create_ec2 <amiId>
"""

args = docopt(doc)

aws = AWSCoreModule.aws

if args["create_s3"]
	bucket = args["<bucket.name>"]
	AWSCoreModule.create_s3(aws, bucket)
end

	

