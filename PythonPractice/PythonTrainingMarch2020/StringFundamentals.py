# String Fundamentals
"""
Str1 = "This is python training class"

# Print whole string in the upper case
print(Str1.upper())

# Lower case
print(Str1.lower())

#Get Count of character
print(Str1.count('t'))

print(Str1.find('python'))

Str2 = "Tomahawk"
Str3 = "Jad"

Str4 = "ja".join(Str2)
print(Str4)

#Get length of string
print(len(Str2))


#Write a string multiple times

nums = "#"
print(nums*10)

# Replace the string

temp1 = "Temp data is showing here"
temp2 = "replace"
result = temp1.replace('data', temp2)
print(result)



# If else condition or conditional statements


# Check any character available in the string
"""


# char = 'r'
# Str4 = "rule are difined in the book"
#
# result_count = Str4.count('p')
# print(result_count)
#
# if char in Str4:
#     print("Character Found :", char)
# else:
#     print("Does not found :", char)
#

######################################
# get the count of each char in the given string

new_str = "get given string"
dict1 = {}

# for smita in new_str:
#     print(smita)

# for var in new_str:
#     print(var)
#     if var in dict1:
#         dict1[var] += 1
#     else:
#         dict1[var] = 1
#
# print("result :", dict1)
#

# iF "given" is available in the string then reverse it.

new_str1 = "get given string"
input_word = 'given'
end_result = "get nevig string"
"""
1. Separate each word. : str.split() -> list of words
2. Go through each word.-> for word in word_list
3. Check input word available in the list. -> if input_word == input word:
4. reverse the given word -> word[::-1]
"""

word_list = new_str1.split(" ")
result_str = ""

for word in word_list:
    if input_word == word:
        result_str = result_str+" "+input_word[::-1]
    else:
        result_str = result_str+" "+word

print("result_str :", result_str)


# problem3 : get count of each character from in the matching word.

input_str3 = "Hello CoronaHowAreYou, please go away"
input_word = 'CoronaHowAreYou'
result_data = {'C':1, '0':3, 'a':1, 'A':1, 'n':1, 'r' :2, 'Y': 1, 'H':1, 'w':1}









