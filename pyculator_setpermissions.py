#!/usr/bin/python
import os, sys, stat

# assign a filename to the variable for recursive use. think about how you would ingest input from the user.
strFile = “./testfile.txt”

# read the manual for definitions.
st = os.stat(strFile)
strPermission = oct(st.st_mode)
strPermission = strPermission[3:] # we are cutting out the first three characters since we only want the last FOUR.

# output our information to the user in a clean format
print(“Permissions for “ +  strFile + “ are: “ + strPermission)
