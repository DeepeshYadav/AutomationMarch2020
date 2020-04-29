import re
with open('testid_file.txt', 'r+') as file:
    data = file.read()
    result = re.findall('([0-9]+)', data)
    print(result)
    print(len(result))
