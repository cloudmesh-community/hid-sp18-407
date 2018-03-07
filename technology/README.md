# Setup

First you need to check out the repositories. 

    mkdir -p ~/github/cloudmesh-community
    cd ~/github/cloudmesh-community
    git clone https://github.com/cloudmesh-community/hid-sample.git

You will not need to pull the hid-sample directory on a weekly
schedule with

    git pull

to see new additions and improvements, as expected from any open
source project.  Now clone your own repository either with ssh or
https. SSH naturally requires you to have uploaded your public key to
github. Let us use for now https.

Let us assume your hid is hid-sp18-999. You need to clone your own
repo as follows

    cd ~/github/cloudmesh-community
    git clone https://github.com/cloudmesh-community/hid-sp18-999.git
    cp -r hid-sample/technology hid-sp18-999
    
Warning: Please make sure there is no / after the technology directory
name.
  
Next you need to go into that directory and correct them with your
information. Make sure to not checkin the sample files from
hid-sample, but modify them. If we find sample files from hid-sample
in your github repository we will deduct points.

After you have modified your files you want to make a test compile with

    cd ~/github/cloudmesh-community/hid-sp18-999/technology
    make
    
You will see that in dest a pdf file is created that you can look at

You will need in all five abstracts in the technology folder.   Each file name should have the following format:

    abstract-<technology>.tex

as well as the bibliography file

    hid-sp18-999.bib

Make sure all references are changed to include your hid prefix as a
label. For more information see the text in abstract-xms.tex

Before you commit, delete the following files that are should be in your directory:

    hid-sample.bib
    abstract-xms.tex



