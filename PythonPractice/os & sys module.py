import os

# Get Current working directory info
dirnamepath = os.getcwd()
print(dirnamepath)

# Change working directory
# -> os.chdir("C:\\")

# Get list of directories and file on given location.
# -> print(os.listdir("C:\\"))

# Create directory on given location
# -> os.mkdir("C:\\DataFile1")

# Create multi folder
# -> os.makedirs("C:\\NewFolder1\\NewFolder2\\NewFolder3")

# Remove directory
# -> os.removedirs("C:\\NewFolder1")

# Join path of the system
# -> print(os.path.join("C:\\NewFolder1", "file1.txt"))

# get os name
# -> print(os.name)

# rename file name
# -> os.rename("file1.txt", "file1_new.txt")




#################### Sys Module ##########################
"""
import sys

sys.argv[1]
sys.path
sys.version
os.system()

"""