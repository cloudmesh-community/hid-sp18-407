# Plain Hadoop install

## ssh into Rasp Pi: 
'''

ssh pi@[IP]

pi 1  192.168.0.10 - master
pi 2  169.254.217.72 - node 2
pi 3  169.254.95.250 - node 3

Master is Raspberry pi 1

Connected three RPis via ethernet switch. 
Obtain IP addresses for all three RPis - 
'''
pi@raspberrypi: ~$ ifconfig
eth0: flags...
inet 169.254.95.250
...
'''
or you can obtain via:
''' 
pi@raspberrypi: ~$ hostname -I
'''

'''
enable ssh across all three nodes
ssh into pi = 
ssh pi@<IP>

while still in home dir 

pi@pi1:/ $ ssh-keygen 

"Enter file in which to save the key):" hit enter
This will create the directory /home/pi/.ssh
enter a passphrase - do not leave blank
...
your ID has been saved in /home/pi/.ssh/id_rsa
your public key has been saved in /home/pi/.ssh/id_rsa.pub
...

id_rsa.pub file is your public key. 
