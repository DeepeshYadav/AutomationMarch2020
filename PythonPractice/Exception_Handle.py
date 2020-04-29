def divide_by_zero():
    try :
        a = 0
        b = 1
        c = b/a
    except Exception as e:
        print(e)

#divide_by_zero()

def index_out_of_range():
    list1 = [2, 6, 8]
    try:
        print(list1[2])
    except Exception as e:
        print(e)
    else:
        print("Task Completed successfully")
    finally:
        print("Failed with Exception")

index_out_of_range()



'''
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

'''
