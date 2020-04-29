# Example1 :

data = lambda x:x**2
print(data(5))

#
list2 = [3, 5, 6, 7]

result = list(map((lambda X : X**2), list2))
print(result)

# map example2

list_str = ['hello', 'geek', 'ogo', ]
result_str = list(map(lambda x: str(x).upper(), list_str))
print(result_str)
#----------
list_str2 = ['hello', 'geek', 'ogo', 'ata' ]
result_str2 = list(filter(lambda x: (str(x)[::-1] == x), list_str2))
print(result_str2)



#----------------------
def fun2(list):
    for i in list:
        print(i**2, end=" ")

fun2([3, 5, 7, 8])

def fun(n):
    return n**2
# using map function can eterate through any list of data
result3 = list(map(lambda x : fun(x), list2))
print(result3)

#######################################
# Filter : It will return list of true values:

List3 = [1, 3, 6, 34, 65, 73]

filter_result = list(filter(lambda x : (x>2), List3))
filter_result1 = list(filter(lambda x : (x%2 == 0), List3))
filter_result3 = list(filter(lambda x : (x%2 != 0), List3))


print(filter_result)
print(filter_result1)
print(filter_result3)





