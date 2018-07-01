import glob
import os

hids = glob.glob("../../hid-sp18-*")

for d in hids:
    if os.path.isdir(d):
        command = ("cp Makefile {d}/paper".format(d=d))
        print (command)
        os.system(command)
