import sys
import os
import random
"""
def get_prime_number():
    argument = sys.argv
    print(argument)
    if len(argument) > 1:
        for i in range(2, int(argument[1])):
            flag = 0
            for j in range(2, i-1):
                if i%j == 0:
                    flag =1
                    break
            if flag == 0 :
                print(i)
    else:
        print("Please provide appropriate interger")

get_prime_number()


# Get platform name

print(sys.platform)
print(sys.path)
import os

def run_command():
    platform = sys.platform
    if platform == "win32":
        os.system("dir")
    elif platform == "Linux":
        os.system("ls")

#run_command()

# Python Version
print(sys.version_info)


print("Hello")  # Big O(1)

for i in range(5): # Big O(n)
    print(i)
count = 0
for i in range(5):  # Big O(n*2)
    for j in range(5):
        print(i, j)
        count = count +1

print(count)


# system exit code:

def run_command_new():
    platform = sys.platform
    if platform == "win33":
        os.system("dir")
        sys.exit(0)
    else:
        print("please run program in aprorpaite platform")
        sys.exit(1)

run_command_new()

"""
list1 = [3, 5, 7, 9]
print(random.choice(list1))

list2 = [3, 5, 7, 8, 9, 1]
random.shuffle(list2)
print(list2)


print(random.sample([3, 6, 8, 9, 6, 8, 2], k=4))
str1 = "Hello ITPD Students"
print(random.sample(str1[10:], k=4))