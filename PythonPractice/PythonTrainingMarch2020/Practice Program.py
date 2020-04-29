#Problem1 : find out length of string : using loop
#input_str = "Hello World"


# Problem 2 : Find out longest word in given sentence
# input str : "Hello This Python  Training Program"
# output : 'Training'


# Problem 3: find out smallest word in the given string :using loop
# input str : "Hello This Python  Training Program"
#output : 'This'


#Problems 4: Print whole string in reverse order :
#input str = "Hello Guys"
#output = "Guys Hello"


#Problem1 : find out length of string : using loop
input_str = "Hello World"

count = 0
for var in input_str:
    #print(var)
    count = count + 1
print(count)

#Problems 4: Print whole string in reverse order :
#input_str1 = "Hello Guys"
#output1 = "Guys Hello"
#output2 = 'syuG olleH'

#output2
#1.  go through each char from negative index. for var in range(-1, -limit, -1)
# temp = temp + var
# print(temp)

input_str1 = "Hello Guys"
#output2 = 'syuG olleH'
reverse = ""
for var in range(-1, -len(input_str1) -1, -1):
    reverse = reverse + input_str1[var]
    #print(reverse)

print(reverse)


#program 2
input_str_new = "Hello Guys"
#output1 = "Guys Hello"
# 1. split to seperate each word
# for through each word in negative

word_list = input_str_new.split(" ")
#print(word_list)

temp_str = ""
for word in range(-1, -len(word_list) -1, -1):
    #print(word)
    temp_str = temp_str +" "+ word_list[word]
    #print(temp_str)

print(temp_str)





# Problem 2 : Find out longest word in given sentence
input_str4 = "Hello This is Python Training Program"
# output : 'Training'


"""
steps to resolve
1. Split each word using split function. ->  input_str4.split(" ")
2. Go through each word and find its length. -> for word in word_list.
3. get legth of each word -> len(word)
4. compare each word length and get max length.
"""

word_list = input_str4.split(" ")
length_list = []

for word in word_list:
    length_list.append(len(word))

print(word_list)
print(length_list)

#max length
max_len = length_list[0]
for var in length_list:
    if var > max_len:
        max_len = var

print(max_len)
max_index = length_list.index(max_len)
print(word_list[max_index])

#small length
min_len = length_list[0]
for var in length_list:
    if var < min_len:
        min_len = var

print(min_len)
min_index = length_list.index(min_len)
print(word_list[min_index])





result = lambda x , y : x+ y

print(result(10, 20))
