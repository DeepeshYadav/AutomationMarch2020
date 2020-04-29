import sys
"""

def get_file_perameters():
    print("All parameters pass to the file", sys.argv)
    if len(sys.argv) > 2:
        filename = sys.argv[1] if sys.argv[1] is not None else "No Data"
        filemode = sys.argv[2] if sys.argv[2] is not None else "No Data"
        print("FileName:", filename, "FileMode:",filemode )

        filedata = open(filename, filemode)
        filecontent = "returns a list of command line " \
                  "arguments passed to a Python script. " \
                  "The item at index 0 in this list is always " \
                  "the name of the script. " \
                  "The rest of the arguments are stored at the subsequent indices."
        filedata.write(filecontent)
        filedata.close()
    else:
        print("File name is not provided")

get_file_perameters()


# Get platform via sys module


platform = sys.platform
print("platform:", platform)
if platform == "win32":
    print("This is windows machine")
elif platform == "Linux":
    print("This is linux platform")
else:
    print("Could not find the platform")



# Get the windows path:
print("system path:", sys.path)


# Get python version
print("system version :", sys.version)

"""
# Get exit function

print("Exit Function")
result = sys.exit(1)
print(result)

