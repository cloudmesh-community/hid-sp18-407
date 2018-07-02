
Installing Scala Build Tool
https://www.scala-sbt.org/0.13/docs/Installing-sbt-on-Linux.html

codeblock
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt

Install Cassandra 

http://cassandra.apache.org/download/
Use instructions from Deb
start cassandra with - sudo service cassandra start
stop cassandra with - sudo service cassandra stop

Clone the killrweather dir

cd into the data dir
start the cql shell - just type cql

