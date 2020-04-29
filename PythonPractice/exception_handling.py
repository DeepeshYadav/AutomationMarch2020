
def handle_list_error():
    try:
        list1 = [2, 4, 6, 8]
        print(list1[4])
    except:
        print("Given index is not available")

#handle_list_error()

def handle_list_error1():
    try:
        list1 = [2, 4, 6, 8]
        print(list1[4])
    except Exception as e:
        print("Given index is not available")
        print("Caugth Exception : {}".format(e))

#handle_list_error1()

def  get_success_msg():
    a = 10.0; b = 20
    try:
        c= b//a
    except Exception as e:
        print("Caugth Exception :{}".format(e))
    else:
        print("Operation Successfully Executed :", c)

#get_success_msg()

def finally_except():

   try:
        dict2 = {}
        list1 = [(3, 5), 5, 7, 8]
        list2 = [3, 5, 7, 9]
        list3 = [5, 66, 7, 3]
        dict2 = dict(zip(list1, list2, list3))
        tuple1 = tuple(zip(list1, list2, list3))

        print(dict2)
        print(tuple1)
   except Exception as e:
       print("Caugth Exception {}". format(e))

   finally:  # This block will be executed in condition,
             # Weather previous code raise exception or not.
        tuple3 = (2, 4, 5)
        for i in tuple3:
            print(i**2, end=" ")

#finally_except()

def get_file_content():
    try:
        filedata2 = open("file2.txt", 'r+')
        filedata2.write("Harish Jag Jao")
        filedata2.close()
    except Exception as e:
        print(e)
    finally:
        with open("file1.txt", 'w+') as Filedata:
            Filedata.write("New Content, Harish")
#get_file_content()

def user_defined_exception():
    list1 = ['a', 'b', 'A', 'B', 'C']
    for i in list1:
        if i.islower():
            print(True)
        else:
            # raise user defined exceptions
            raise Exception("Can't Accept Capital Value")

#user_defined_exception()


# Assertion

def get_squar_value():
    list1 = [2, 4, 7, 8, 9]
    list2 = [4, 16, 50, 64, 81]
    list3 = []
    for i in list1:
        list3.append(i**2)
    if list2 == list3:
        return  True
    else:
        return  False

#print(get_squar_value())

def verify_functionlity():
    assert get_squar_value() == False
    print("Successfully Executed")


verify_functionlity()
## Formating Example :


"""
print("Given value of a :{0} and b:{1}".format(a, b))
Given value of a :20 and b:30
>>> print("Given value of a :{} and b:{}".format(a, b))
Given value of a :20 and b:30
>>> print("Given value of a :{1} and b:{0}".format(a, b))
Given value of a :30 and b:20

"""