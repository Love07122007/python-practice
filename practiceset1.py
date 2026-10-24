#wap to print the poem
#print("twinkle twinkle little star how i wonder what you are up above the world so high like a diamond in the sky twinkle twinkle little star how i wonder what you are")
#4. Write a python program to print the contents of a directory using the os module. Search
#online for the function which does that.

import os

# Specify the directory path
path = "."

# Get the list of files and folders
contents = os.listdir(path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)