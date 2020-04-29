from handle_file import handle_file

def read_whole_file():
    f = open("file1.txt", "r")
    data = f.read()
    print(type(data))
    print(data)

def read_file_with_lines():
    f = open("file1.txt", 'r')
    data = f.readlines()
    print(data)
    for line in data:
        print(line)

def read_file_with_lines():
    b = handle_file("file1.txt", "r")
    print("Filename :", b.name)
    print("File Mode :", b.mode)
    print("Check if File closed on not", b.closed)

#read_file_with_lines()

# In write file mode "W"
# It will overwrite the existing file available.
# I Creates file, if it is not available on the given location
def write_file():
    d = handle_file("file2.txt", "w")
    print(d.writable())
    d.write("This is python class")
    d.close()
    print(d.closed)


#read_file_with_lines()
#write_file()

# -> Next mode is open file in append mode.
# -> It starts modify file from end.
# -> mode+ :  open file in both read and write mode
# -> Seek(0,2) : it sets the pointer to read the file.
#(0, 0) : Beginning, (0, 1) : current pointer, (0, 2) : End of the file.
def append_data_to_file():
    p = handle_file("file1.txt", "a+")
    p.write("\n Data Appended to the file")
    print(p.tell())  # It will tell user the current location of pointer
    p.seek(0, 0)
    data = p.read()
    print(data)
    p.close()

def context_manager(filename):

    with open(filename, "r") as file:
        data = file.read()
        print(data)
        print("is file closed inside:", file.closed)
        print(file.tell())
        file.seek(0, 0)
        print(file.tell())
        lines = file.readlines()
        #print(lines)
        # Interate through all lines of file
        for i in range(len(lines)):
            print(i, ":", lines[i])
"""
    with open(filename, 'a+') as file2:
        print("filemode", file2.mode) # display file mode e.g a
        print("filename", file2.name) # display file line

        str = 'This data should place in the end of file'
        file2.write(str)  # Append given content to the file
        file2.seek(0, 0) # Set pointer to the beginning
        read_data = file2.readlines()
        print(read_data[-1])  # It will read last line of file
"""
context_manager("file1.txt")

import xlrd
#  command to install xlrd module
#  -> pip install xlrd

def read_excel_file_content():
    excel_file = "Test_Data.xlsx"
    wb = xlrd.open_workbook(excel_file)
    sheet = wb.sheet_by_index(0)  # get sheet dat by its index
    colns  = sheet.ncols
    rows  = sheet.nrows
    valueofcell = sheet.cell_value(0, 0)  # get cell values by index
    print(colns) # print number of coloms
    print(rows)  # print number of rows
    print(valueofcell)  # print cell value

    for i in range(rows):
        print("\n")
        for j in range(colns):
            print(sheet.cell_value(i, j), end=" ")

    #rows = 5, colns = 3
    # i = 0 , j=0 , 1, 2, 3 , 4
#read_excel_file_content()

# csv module to read data from csv file.
import csv

def read_csv_file():
    csv_data = open("test_data.csv")
    output = csv.reader(csv_data)
    datalist = list(output)
    print(datalist[0][1])

#read_csv_file()
#append_data_to_file()

# commands to get all modules installed
# -> pip freeze >> requirements.txt

# command to install all dependecies on the system
# -> pip install -r requirements.txt




# Assingment
"""
1. Write a Python program to read an entire text file. 
2. Write a Python program to read first n lines of a file. 
3. Write a Python program to append text to a file and display the text. 
4. Write a Python program to read last n lines of a file. 
5. Write a Python program to read a file line by line and store it into a list. 
6. Write a Python program to read a file line by line store it into a variable.
7. Write a Python program to read a file line by line store it into an array. 
8. Write a python program to find the longest words. 
9. Write a Python program to count the number of lines in a text file. 
10. Write a Python program to count the frequency of words in a file. 
11. Write a Python program to get the file size of a plain file. 
12. Write a Python program to write a list to a file. 
13. Write a Python program to copy the contents of a file to another file . 
14. Write a Python program to combine each line from first file with the corresponding line in second file. 
15. Write a Python program to read a random line from a file. 
16. Write a Python program to assess if a file is closed or not. 
17. Write a Python program to remove newline characters from a file. 
"""