#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/my_code/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/my_code/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/my_code/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

