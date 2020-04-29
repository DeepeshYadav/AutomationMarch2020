#filename = 'read_data.txt'
'''

file = open('read_data.txt', 'r')
data = file.read()
#print(data)
file.close()

# Read file lines
file_lines = open('read_data.txt', 'r')

lines = file_lines.readlines()

print(lines)

for line in range(0, len(lines), 2):
    print(lines[line])
'''

# write file
# 1. write, create new file if it is not available
# 2. write, overwrite the file content , it some content is already available.
def read_write(filename):
    str1 = """jkhkfjsahdfkljsahdlkj
    \n line 2 data
    \n line3 data and its input"""*20

    file = open(filename, 'w+')

    file.write(str1)

    file.close()

read_write('writefile.txt')


# Append the file
# IF file is not available, then it will create the file
# It will append content at the end of the file.
# It does not overwrite the existing content

def append_file(filename):
    file = open(filename, 'a+')
    #      open(filename, filemode)

    print(file.mode)
    print(file.name)

    file.write("\n Third Attempt to write")
    file.close()

#append_file('append_file.txt')


def append_file_as_start(filename):
    file = open(filename, 'r+')
    #      open(filename, filemode)

    print(file.tell())
    file.seek(0, 0)
    print(file.tell())
    file.write("Our new data\n")
    file.close()

append_file_as_start('append_file.txt')

# Context manager : Context manager has default enter and exit method inside
# do need to close the file explicitly

def context_text(filename1, filename2):
    with open(filename1, 'r') as file1:
        file1data = file1.read()

    with open(filename2, 'a') as file2:
        file2.write(file1data)

    with open(filename2) as file3:
        data = file3.read()

    print(data)


#context_text('read_data.txt', 'write_data.txt')


# Read last 5 lines of file.

def read_last_n_lines(n, filename):
    with open(filename, 'r+') as file:
        file_lines = file.readlines()

    for i in range(-n, 0, 1):
        print(file_lines[i])

read_last_n_lines(5, 'write_data.txt')