# Website for testing regx : https://www.regextester.com/

import re

# Example 1
global inputstr
inputstr = "Create a class with three methods which give complete detail of a carresult."

def findall_example():
    # Findall method return list of matching string
    # Either return empty list
    result = re.findall("a", inputstr)  # result how many a in the given string
    result2 = re.findall("c\w+ ", inputstr) # return all the words which starts with c
    result3 = re.findall("Find", inputstr) # it will return empty list if pattern did not match

    print(result)
    print(result2)
    print(result3)

#findall_example()

def search_examples():
    # Search method will return the object if it is available in string
    #  It always look for first occurrence
    # Either return None

    result = re.search("three", inputstr)
    result2 = re.search("three123", inputstr)
    print(result)
    print(result2)

#search_examples()

def sub_example():
    # sub method replace the word in given string and return the new string generate
    result = re.sub("three", "ITPD", inputstr)
    # Three will be replace with ITPD
    print(result)
    print(inputstr)

#sub_example()

def split_example():
    # split method , split the string by given pattern
    str2 = "www.google.com"
    result = re.split("\Wa+", inputstr)
    result2 = re.split("\sa\s", inputstr)
    print(result)
    print(result2)

#split_example()

def get_dates_from_data():
    str = " today's date is 12-07-2019 and out event scheduled on 20-07-2019"
    result = re.findall("\d\d-\d\d-\d\d\d\d", str)
    print(result)

    # get the repeatative value from string

    str2 = "abccc abc adad ccddeded"
    result2 = re.findall("\w*c{2}\w+", str2)
    print(result2)


#get_dates_from_data()

def get_email_id_data():
    data = " a1@gmail.com  this email is not valid a2@test.com  valid@yahoo.com"
    result = re.findall("\S+@\S+", data)
    print(result)


get_email_id_data()
