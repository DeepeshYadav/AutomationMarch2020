import re

str = "All the data can manipulated"
result = re.findall("at", str)
print(result)


result2 = re.search("data", str)
print(result2)
print(result2.start())

result3 = re.split("\W", str)
print(result3)

########

result4 = re.sub("data", "ITPD", str)
print(result4)

result5 = re.search("S+", str)
print(result5)

str1 ="750-737-5027 this mobile contact we can connect 750-737-5077  Hello shubhamg199630@gmail.com Rohit neeraj@gmail.co"
result6 = re.findall("\d\d\d-\d\d\d-\d\d\d\d", str1)
print(result6)

result7= re.findall("[a-zA-Z0-9.]\W", str1)
print(result7)

result8 = re.findall("\S+@\S+", str1)

print(result8)



