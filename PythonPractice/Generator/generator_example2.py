import time
import random
import psutil


namelsit = ['rahul', 'john', 'mary', 'Deo', 'park']
addresslist = ['pune' , 'banglir', 'gwqlior', 'bhopal']
occupation = ['doctor', 'engineer', 'lawyer']

def population(people_num):
    result = []
    for i in range(people_num):
        people = {
            'name': random.choice(namelsit),
            'address': random.choice(addresslist),
            'occupation': random.choice(occupation)
        }
        result.append(people)

    return result


def gen_population(people_num):
    result = []
    for i in range(people_num):
        people = {
            'name': random.choice(namelsit),
            'address': random.choice(addresslist),
            'occupation': random.choice(occupation)
        }
        result.append(people)

    yield result

# t1 = time.time()
# memory1 = psutil.virtual_memory()
# m1 = (memory1[3]/1024/1024)
#
# data = population(3456700)
#
# memory2 = psutil.virtual_memory()
# m2 = (memory2[3]/1024/1024)
# t2 = time.time()
# print(t2-t1)
# print(m2-m1)

t3 = time.time()
memory3 = psutil.virtual_memory()
m3= (memory3[3]/1024/1024)

data2 = gen_population(3456700)
t4 = time.time()
memory4 = psutil.virtual_memory()
m4 = (memory4[3]/1024/1024)


time = t4-t3
print(time)
print(m4-m3)
