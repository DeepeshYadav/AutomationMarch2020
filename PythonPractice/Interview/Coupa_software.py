# Question 1 : Input : bcdabc
# Output = abcdbc

import string
def manipulate_string(input):
    result = ""
    char_list = list(string.ascii_lowercase)
    temp = 0
    extra = ""
    input_list = list(input)
    length = len(input)

    while temp < length:
        #print("input list in the start:", input_list)
        small = input_list[0]
        #print("small :", small)
        for char in input_list:
            if char_list.index(char) < char_list.index(small):
                small = char
        #print(small)
        if small in result:
            extra = extra + small
            input_list.remove(small)
        else:
            result = result + small
            input_list.remove(small)
            #print("input list in the end:", input_list)

        temp += 1

    result = result + extra
    return result


print(manipulate_string('bbcdbaedffg'))

# Question 2 : Get all possible combination of
# All three number multiplication should be given number


def get_all_possible_combination(num):

    comb_list = []
    for i in range(num):
        for j in range(i):
            for k in range(j):
                if i*j*k == num:
                    comb_list.append((i, j, k))
                else:
                    continue

    print(comb_list)
get_all_possible_combination(18)

# Question 3 : convert decimal to hexa decimal number

def decimal_to_hexadecimal_(decimal):
    hex_output = ''
    code_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15: 'F'}

    while decimal > 16:
        output = decimal//16
        hex_output = hex_output + str(output)
        decimal = decimal%16

        if decimal > 9 and decimal < 16:
            if decimal in code_dict:
                hex_output = hex_output + code_dict[decimal]
            else:
                continue
        else:
            hex_output = hex_output + str(decimal)

    print(hex_output)

decimal_to_hexadecimal_(266)


xml='''<website>
        <name>Codespeedy</name>
        <article>Related to programming</article>
        <message>You can learn easily from codespeedy</message>
    </website>'''
import re
import json


def xml_to_json(xml):
    main_dict = {}
    result = re.findall('.*', xml)
    for data in result:
        output = re.findall("^<.*>{1}", str(data).lstrip())
        print("output :",output)

xml_to_json(xml)

