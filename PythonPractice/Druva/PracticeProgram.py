# 1. Get Highest some of any number of given array:

def get_highest_some_two_number(A):

    maxsum = 0
    for i in A:
        n=0
        while n < len(A)-1:
            if i == A[n]:
                n = n + 1
                continue
            else:
                sum = i + A[n]

            if sum > maxsum:
                a = i
                b = A[n]
                maxsum = sum
            n = n + 1
    return a, b, maxsum


#A = [4, 6, 8, 9, 23, 78, 35, 101]
#first, second, maxsum = get_highest_some_two_number(A)
#print("First: {},  Second:{},  Maxsum: {}:".format(first, second, maxsum))


# 2. Replace str2 with str3 from str1 if it is found.
def replace_string(s1: str, s2 : str, s3: str):
    s4 = ""
    if s2 in s1:
        print("Replacing the string")
        s4 = s1.replace(s2, s3)

    print(s4)
    print(s1)

str1 = "Hello Friend My Name Ganesha tum rahna sath hamesha"
str2 = "My Name Ganesha"
str3 = "Hanuman Veer Bajrang"
#replace_string(str1, str2, str3)

# 3. Calculate days between two dates.

from datetime import date
def get_days_bw_two_dates():
    d1 = date(2008, 9, 23)
    d2 = date(2008, 8, 20)
    diff = d1 - d2
    print(diff.days)


#get_days_bw_two_dates()


def prime_number_program(n):
    for i in range(2, n):
        if n%i == 0:
            print("Its not an prime number")
            break
    else:
        print("It's Prime number")

#prime_number_program(13)

def prime_number_optimize(n):
    primes = [2, ]

    for i in range(3, n, 2):
        isprime = True
        for j in primes:
            if i%j == 0:
                isprime = False
                break

        if isprime:
            primes.append(i)

    print(primes)


#prime_number_optimize(50)

# Binary Search Apply on list:

def binary_search(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high)//2
        if key == A[mid]:
            return True
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid -1

    return False

A = [4, 6, 8, 9, 23, 45, 67]
key = 10
#print(binary_search(A, key))


def sum_of_value(num1:str, num2 : str, num3: str):
    return num1 + num2 + num3

def sum_of_value(num1:int, num2 : int):
    return num1 + num2


#print(sum_of_value(234, 567))

#print(str.__add__('5', '77'))
#print(int.__add__(6, 8))


def verify_attemp_revers(input1, input2, input3):
    outstr = ""
    attemp = 0
    while attemp < 5:
        for i in range(1, input2+1):
            outstr = outstr +  input1[-i]
            print(outstr)
        outstr = outstr + input1[:-input2]
        input1 = outstr
        attemp = attemp + 1
    return attemp


print(verify_attemp_revers("HelloData", 2, 3))