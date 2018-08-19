# Install Apache Kudu
This tutorial will demonstrate two ways to install Kudu on Linux Ubuntu 16.04 (Xenial).

Kudu is a columnar distributed data store that is designed to for high-throughput analytics while providing write capabilities on row-level data.

##System Requirements
The first step is to ensure that our system meets minimum requirements:

- Hardware: 
- For VM: 64-bit operating system
- Req 3

Second, we can decide which of the two recommended ways we would like to install and/or run Kudu: either via Kudu quickstart VM, or via command line for additional configuration options. The command line script can be automated in the case of deploying several Kudu instances.

Additionally, Apache recommends at least but ideally three hosts to increase fault tolerance, and at least three tablet servers if replication is being used. Here we will use one master and three tablet servers. 

##Installing Via Command Line

1. Ensure the required libraries are installed, which include :
```sh
$
$
$

```
