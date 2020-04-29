def readfile():
    file = open("file2.txt", 'r+')
    read_data = file.read(10)
    print(read_data)
    print(file.tell())
    read_data2 = file.read(30)
    print(read_data2)
    file.seek(0, 0)
    #print(file.readlines())
    #print(file.tell())
    file.close()


#readfile()


def writefile():
    str = "Data which we write into the file"
    filedata = open("file2.txt", 'w+')
    filedata.write(str)
    filedata.tell()
    print(filedata.read())

#writefile()

def appendfile():
    #str = "Data which we write into the file"
    filedata = open("file2.txt", 'a+')
    filedata.write("\n New content added in end of file2")
    filedata.readlines(50)
    filedata.seek(0, 1)
    filedata.write("\n add data in the beginning2")
    print(filedata.tell())
    print(filedata.read())
    filedata.close()

#appendfile()


def readfile():
    f = open("file2.txt", 'r')
    data = f.read().split()
    print(data)
    max_len = len(max(data, key=len))
    print(max_len)
    longest_word = [w for w in data if len(w) == max_len]
    print(longest_word)

#readfile()
"""
list= [3, 6, 8, 19, 20]
maxvalue = list[0]
for i in list:
    if i > maxvalue:
        maxvalue = i
print(maxvalue)

min = list[0]
for j in list:
    if j < min:
        min = j
print(min)
"""


import xlrd

def read_excel_file():
        filepath = "Test_Data.xlsx"
        wb = xlrd.open_workbook(filepath)
        sheet = wb.sheet_by_index(0)
        #data = sheet.cell_value(0, 0)
        #print(data)
        rows = sheet.nrows
        coln = sheet.ncols
        for i in range(rows):
            print("\n")
            for j in range(coln):
                print(sheet.cell_value(i, j), end=" ")
        print("\n")
        print("#"*50)
        for i in range(sheet.nrows):
            print(sheet.row_values(i))

#read_excel_file()

import json
def read_write_json_file():
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })

    with open('data.txt', 'w') as outfile:
         json.dump(data, outfile)

    with open('data.txt') as json_file:
        data = json.load(json_file)
        print(data['people'])
        print(type(data['people']))
    #     for p in data['people']:
    #         print('Name: ' + p['name'])
    #         print('Website: ' + p['website'])
    #         print('From: ' + p['from'])
    #         print('')
    ###########################################
    # # filedata = open('data.txt', "r")
    # json_data = json.loads(filedata)
    # print(filedata)
    # print(type(filedata))
    # print(filedata['people'])
#read_write_json_file()

import csv
def read_csv_file():
    csv_data = open("test_data.csv")
    output = csv.reader(csv_data)
    print(list(output))

#read_csv_file()

import xml.etree.ElementTree as ET

def read_xml_file():
    tree = ET.parse('tesgt_xml.xml')
    root = tree.getroot()
    print(root.tag)

read_xml_file()
