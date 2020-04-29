"""
def lengthOfLongestSubstring(s: str) -> int:

    if s == " ":
        return 1
    else:
        word_list = []
        tempword = ""
        for char in s:
            print('char :', char)
            if char in tempword:
                word_list.append(tempword)
                tempword = char
            else:
                tempword = tempword + char

        word_list.append(tempword)
        max_len = 0
        for word in word_list:
            if len(word) >  max_len:
                max_len = len(word)
            else:
                continue

        return max_len, word_list


print(lengthOfLongestSubstring(' '))




def total(initial =5, *num, **key):
    count = initial
    print('count:', count)
    for n in num:
       count+=n
    for k in key:
       count+=key[k]
       return count
print(total(100,2,3, clouds=50, stars=100))




class Count:
   def __init__(self, count=0):
      self.__count=count
a=Count(2)
b=Count(2)
print(id(a)==id(b), end = '' '')

c= "hello"
d= "hello"
print(id(c)==id(d))



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        else
            word_list = []
            tempword = ""
            for char in s:
                if char in tempword:
                    word_list.append(tempword)
                    tempword = tempword[tempword.index(char)+1:] +char
                else:
                    tempword = tempword + char
            word_list.append(tempword)
            max_len = 0
            for word in word_list:
                if len(word) >  max_len:
                    max_len = len(word)
                else:
                    continue

        return max_len, word_list

obj = Solution()
print(obj.lengthOfLongestSubstring('dvdf'))



# Median of two sorted array
from statistics import median
def findMedianSortedArrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    srt = sorted(nums1)
    print(median(srt))
    print(srt)
    n = len(srt) // 2
    if len(srt) % 2 == 0:
        return (srt[n - 1] + srt[n]) / 2
    else:
        return srt[n]



list1 = [3]
list2 = [-1, -2, -3]

print(findMedianSortedArrays(list1, list2))


# Find the loggest palindrom string

def longestPalindrome(s: str) -> str:
    max_value = 0
    temp = ""
    long_word = ""
    if len(s) == 1:
        return s
    else:
        for i in range(len(s)):
            temp = s[i]
            temp2 = temp
            if len(temp2) > max_value:
                max_value = len(temp2)
                long_word = temp2
            for j in range(i + 1, len(s)):
                temp2 = temp2 + s[j]
                if temp2 == temp2[::-1]:
                    if len(temp2) > max_value:
                        max_value = len(temp2)
                        long_word = temp2
                    else:
                        continue
                else:
                    continue

        return long_word


str1 ="ac"
print(longestPalindrome(str1))




# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# PAY P ALI S HIR I NG
# P   A   H   N
# A P L S I I G
# Y   I   R

def print_pattern(str1,  row):

    temp = 0
    row_list = []
    while temp < len(str1):
        temp_list = []
        remain = len(str1) - temp
        if remain >= row:
            for i in range(temp, temp+row):
                temp_list.append(str1[i])
                temp += 1

            row_list.append(temp_list)
            if temp < len(str1): row_list.append(str1[temp])
            temp += 1
        else:
            for i in range(temp, temp + remain):
                temp_list.append(str1[i])
                temp += 1
            row_list.append(temp_list)
            temp += 1
    return  row_list

str1 = 'PAYPALISHIRING'
print(print_pattern(str1, 4))

"""



def myAtoi(s: str) -> int:
    import pdb; pdb.set_trace()
    num_str = ""
    if s == "":
        return 0
    elif len(s) > 0 and s[0].isalpha():
        return 0
    for char in s:
        if char in ['-', '+'] or char.isdigit():
            num_str = num_str + char
        elif char == " ":
            continue
        elif char.isalpha():
            continue
        elif char == ".":
            break

    if num_str == "":
        return 0
    elif num_str != '+' and num_str != '-' and int(num_str) > 2 ** 31:
        return 2 ** 31 - 1
    elif num_str != '+' and num_str != '-' and int(num_str) < -2 ** 31:
        return -2 ** 31
    elif num_str == '+' and num_str == '-':
        return 0
    else:
        return int(num_str) if num_str.isalnum() else 0

print(myAtoi(' -42'))