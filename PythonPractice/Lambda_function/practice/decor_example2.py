def decorfunc(func):
    def inner(a, b):
        if a < b:
            a , b = b, a
        return func(a,b)
    return inner

@decorfunc
def div(a, b):
    print(a/b)

#div(8, 6)
###########################################################

#Example2 :

# def function1():
#     print("Hello, I am in function1")
#
# def function2(func):
#
#     print("Hello I am in function2, going to call function1")
#     func()
#
# function2(function1)

def function2(func):
    def inner():
        print("Hello, I am in function2 calling function1")
        func()
    return inner

@function2
def function1():
    print("Hello, I am in function1")

#function1()

###############################################

def greeting_decor(func):
    def inner():
        str = func()
        return str.upper()
    return inner

@greeting_decor
def greeting():
    return "hello, good morning"

print(greeting())

print(greeting.__name__) # It will print inner