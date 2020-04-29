import os
"""
Get Current working directory

-> print(os.getcwd())

Create Folder
-> os.mkdir("C:\\Folder1_new")

for i in range(10):
   os.mkdir("C:\\Folder_loop"+str(i))

create multiple folder
->os.makedirs("C:\\folder1\\folder2\\folder3")

get list of directory adn files

-> fileslit = os.listdir("C:\\")
-> print(fileslit)

-> os.rename("C:\\folder1" , "C:\\folder_renamed")

#change current working directory
    print(os.getcwd())
    
# Get list of all files and directories
    print(os.listdir("."))

# Change current working directory   
    os.chdir("C:\\")
    print(os.getcwd())
    print(os.listdir("."))

#remove directory
    os.remove("C:\\DataFile1")
    os.removedirs("C:\\folder_renamed")

#run windows commmand using python
    data = os.system("dir")
    print("data:", data)


# If if given path is file or directory

input = "data.txt"

if os.path.isdir(input):
    print("It's a directory")
elif os.path.isfile(input):
    print("It's a file")
else:
    print("Unknown Input")
"""
n = 20
for i in range(n):
    for j in range(2, i):
        if i%j == 0:
            break

    else:
        print(i)
"""
import shutil
# copy data from one directory to another
shutil.copy("C:\\DataFile1\\File1.txt", "C:\\Folder1_new")
shutil.rmtree("C:\\folder1")

"""

