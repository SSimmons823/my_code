#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

# move into the working directory
os.chdir('/home/student/my_code/')

# move the file to new destination
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for new file name
xname = input('What is the new name for kerrigan.obj? ')

# rename the current file name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



