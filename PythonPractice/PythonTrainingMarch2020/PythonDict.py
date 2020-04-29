"""
# Python dict, it works with key value pair
# Key can not be duplicate in the list
# Key should be immutable, means should not modify
# Dict in un-ordered data type.
# default in build keyword is dict so don't use as variable

dict1 = {}

dict1['city'] = "Pune"

# duplicate value will be overwrite
dict1['city'] = "Mumbai"

# can not assign list and key
#dict1[[3, 5, 6]] = "random"

dict1[(3, 5, 6)] = "random"

dict1['area'] = 'SaniwarWada, is , best , palce', 'Nisha'

#print(dict1)

# we can assign dict inside the dict

dict2 = {'teacher':20, 'students':50, 'management':20}
dict3 = {'teacher':40, 'students':500, 'management':50}
dict4 = {'teacher':100, 'students':1000, 'management':100}

dict1['Sinhgad School'] = dict2
dict1['Orchid School'] = dict3
dict1['LittleKids'] = dict4

#print(dict1)

# get total teachers in the school
print(dict1['Orchid School']['teacher'])


# Get all keys of dict

#print(dict1.keys())

# Get all the values from dict
#print(dict1.values())


for key, value in dict1.items():
    print(key, ":", value)


# Delete the dict
del dict1
print(dict1)


###########################################################

# string1 = he bad news: from Firefox 55 onwards,
# Selenium IDE will no longer work.
# The reasons for this are complex,
# but boil down to two main causes:
# Browsers are complicated pieces of
# software that are constantly evolving.
# Mozilla has been working hard to make
# Firefox faster and more stable,
# while still retaining the flexibility and ease

word_count = {}
word_list = string1.split(" ")


for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

for key, value in word_count.items():
    print(key, ":", value)
"""

list1 = [1, 6, 8, 9]
result1 = {1:1, 6:36, 8:64, 9:81}

result2 = {'google':1, 'youtube' :2, 'facebook': 4}
result3 = {'gmail' :23, 'microsoft' : 4, 'google': 2}

result2.update(result3)
print(result2)

# how to check key is available in dict
key = 'google'

if key in result2:
    print(True)
    del result2[key]
else:
    print(False)

print(result2)

dict1 = {1:1}
list1 = [2, 4, 5]

# dictionary pop
output = result2.pop('gmail')
print(output)
print(result2)


# list pop
output2 = list1.pop(4)
print(output2)

print(list1)



    
    




