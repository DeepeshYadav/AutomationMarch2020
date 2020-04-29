import random

# -> All possible methods are available in python

#['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
# 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence',
# '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect',
# '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi',
# '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
# '_urandom', '_warn', 'betavariate', 'choice', 'choices',
# 'expovariate', 'gammavariate', 'gauss', 'getrandbits',
# 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
# 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate',
# 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

"""

# get choice from number, It will pick any random number from given list

number = [2, 6, 8, 9]
print(random.choice(number))


# get shuffled number from given list
new_list = [3, 5, 8, 2, 1, 23]
random.shuffle(new_list) # It shuffle the list in place
print(new_list)



# get random number from specific range

print(random.randrange(1, 10, 2)) # print any random number from given range with difference 2
print(random.randrange(0, 100, 5)) # print any random number from given range with 5 difference


# get random string, it will return list of any specified number of characters
print(random.sample("This is random string", k=5))

"""