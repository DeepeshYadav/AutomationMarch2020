# def fun1():
#     print("Harish")
#
import time

def func2(func):
    def inner(args):
        print("Welcome")
        func(*args)
        print("Good Bye")
    return inner()


def fun3(func):
    def inner(*args):
        begin_time = time.time()

        print("begin_time", begin_time, time.localtime())
        func(*args)
        endtime = time.time()
        print("endtime", endtime, time.localtime())
    return inner

#print(func2(fun1))

@fun3
def fun1(n):
    fact = 1
    while n  > 1:
        fact = fact*n
        n = n-1

    print(fact)

fun1(5)