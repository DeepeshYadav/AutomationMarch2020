import xlrd
import os
import shutil

"""
1. Read file Extension from excel sheet. Done
2. Create Files with extension and specific folder. : Done
3. Seperate All files with their extension ; Done
4. Find out files and folder. : Done
5. Copy Specific extension files in extension named folder : Done
"""

def get_data_from_excel(filepath):
    exten_list = []
    print("extension list:", exten_list)
    wb = xlrd.open_workbook(filepath)
    sheet = wb.sheet_by_index(2)
    rows = sheet.nrows
    cols = sheet.ncols
    print("Rows :", rows)
    print("Colns :", cols)
    # interate through the rows
    for i in range(rows):
        print(i, ":", sheet.cell_value(i, 0))
        exten_list.append(sheet.cell_value(i, 0))
    print("extension list:", exten_list)
    return exten_list

#get_data_from_excel("test_data.xlsx")

def create_files_with_different_extension(excel_sheet_path, folderpath, content):
    # Create Directory
    os.mkdir(folderpath)

    # store return data in the variable
    #extension = get_data_from_excel("test_data.xlsx")
    extension = get_data_from_excel(excel_sheet_path)
    list_length = len(extension)
    print("list_length:", list_length)

    for i in range(list_length):
        #Create file path
        filepath = folderpath+"file"+str(i)+"."+extension[i]

        # Create new file and write data inside it
        with open(filepath, "w") as filedata:
            filedata.write(content)

def write_into_text():
    extension = get_data_from_excel("test_data.xlsx")
    with open("newfile_new.txt", "w") as file:
        file.write(str(extension))

#write_into_text()




# content = "My question is, why 3 d" \
#           "ifferent ways of doing this" \
#           "? When should one way be used " \
#           "and not another? Which way is the 'best' (most future-proof or least likely to accidentally exclude" \
#           " a particular system which your " \
#           "program can actually run on)?"
#create_files_with_different_extension("D:\\MultipleFolder1\\", content)

def get_files_with_extsion(folderpath):

    # data list
    data_list = []
    # Get File list
    file_list = os.listdir(folderpath)
    exten_dict = {} # dictionary for extension
    exten_list = [] # list for extension
    for file in file_list:
        exten = file.split(".")
        print("Filename:", exten[0])
        exten_list.append(exten[1])
        print("Extension :", exten[1])
        # check if extension in dictionary and increase the count
        # If not in dictionary add value inside it.
        if exten[1] in exten_dict:
            exten_dict[exten[1]] = exten_dict[exten[1]] + 1
        else:
            exten_dict[exten[1]] = 1

    print(exten_list)
    print(exten_dict)
    print(file_list)
    data_list.append(exten_list)
    data_list.append(exten_dict)
    data_list.append(file_list)
    print(data_list)
    return  data_list

#get_files_with_extsion("D:\\MultipleFolder1\\")

def separate_files_in_folders(folderpath, copy_path):
    files_data = get_files_with_extsion(folderpath)
    extension_dict = files_data[1]
    file_list = files_data[2]
    exten_list = files_data[0]

    # Get all keys from dictionary which are file extensions
    dict_keys_name = extension_dict.keys()
    print(dict_keys_name)

    for i in dict_keys_name:
        # join path with foldername
        dir_path = os.path.join(copy_path, i)
        if os.path.exists(dir_path):
            continue
        else :
            os.mkdir(dir_path)

    # copy files from target to destination folder
    for exten in dict_keys_name:
        print("entens :", exten)
        for file in file_list:
            file_exten = file.split(".")
            if file_exten[1] == exten:
                print("condition true")
                dest_filepath = os.path.join(copy_path, exten)
                src_filepath = os.path.join(folderpath, file)
                shutil.copy(src_filepath, dest_filepath)




#separate_files_in_folders("D:\\MultipleFolder1", "D:\\New\\")

#seperated_file_with_extsion("D:\\MultipleFolder1\\")

content = "My question is, why 3 d" \
          "ifferent ways of doing this" \
          "? When should one way be used " \
          "and not another? Which way is the 'best' (most future-proof or least likely to accidentally exclude" \
          " a particular system which your " \
          "program can actually run on)?"

def file_sepration_program(excel_sheet_path, folderpath, content, copy_path):
    create_files_with_different_extension(excel_sheet_path, folderpath, content)
    separate_files_in_folders(folderpath, copy_path)


file_sepration_program("test_data.xlsx", "D:\\MultipleFolder1\\", content, "D:\\New\\")