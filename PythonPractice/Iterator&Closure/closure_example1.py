#

def function1(msg):
    def function2():
        print("we are in  inner function")
        return msg
    return function2



fun = function1("Hello, Good Morning")
print(fun)

output = fun()
print(output)