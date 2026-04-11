# write a python program to print the contents of a directory using the os module. 
# search online for the function which does that

import os

# specify directory path (use "." for current directory)
path = "/New Folder"

# get list of contents
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)