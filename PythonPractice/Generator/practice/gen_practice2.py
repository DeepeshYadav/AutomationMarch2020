import psutil
import time
import random

name = ['john', 'carry', 'Gabbu', 'Golu', 'Gabbar', 'Sadden', 'Salute']
majors = ['Engineer', 'Doctor', 'architect', 'Manager', 'teamlead']
memory = psutil.virtual_memory()
user_time = time.clock()
print(user_time)

def people_data(people_num):
    result = []
    for i in range(people_num):
        people ={
                    'name' : random.choice(name),
                    'major' : random.choice(majors),
                    'number' : random.choice(8967)
                }
        result.append(people)
    return result


def people_generat(people_num):
    result = []
    for i in range(people_num):
        people = {
                    'name': random.choice(name),
                    'major': random.choice(majors),
                    'number': random.choice(8967)
                }
        result.append(people)
    yield people




