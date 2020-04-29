def function_name():
    list1 = [3, 6, 8, 9, 3, 56, 15, 30]
    list2 = []
    for value in list1:
        if value%3 == 0 or value%5 == 0:
            list2.append(value)

    return list2



#result = function_name()
#print(result)

def print_table(n, name):
    print("Table Owner Name:", name)
    for i in range(1, 11):
        print("{}*{}={}".format(i, n, i*n))



#print_table(12)

sagar = 30
#print_table(sagar, 'sagar')
#print_table(n=sagar, name='sagar')


# function with default value
def reverser_number(n=123):
    revers_num = 0
    while n > 0:
        temp = n%10
        revers_num = revers_num*10 + temp
        n = n //10

    print(revers_num)


#reverser_number(34567)


# function with multiple param

def get_factorial(*args):

    fact_list = []
    for var in args:
        #print("var :", var)
        fact = 1
        for num in range(1, var+1):
            #print('num:', num)
            fact = fact*num
            #print(fact)

        fact_list.append(fact)
    print(fact_list)


#get_factorial(4, 5, 6, 8, 9)


def get_prime_number_list(n):
    prime_list = []
    for i in range(2, n):    # 2, 3, 5, 7,
        if (i%2 ==0 or i%3 == 0 or i%5==0 or i%7 == 0) and (i not in [2, 3, 5, 7]):
            continue
        else:
            print(i, end=" ")

#get_prime_number_list(50)

#global variable
global_age = 10

def global_and_local():
    #local  variable
    age = 20
    global name
    name='sagar'
    print(age)
    print(global_age)
    print(name)


def function2():
    print(global_age)
    print(name)


global_and_local()
function2()