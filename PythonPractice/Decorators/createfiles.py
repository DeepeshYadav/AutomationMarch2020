user_input = input("Please enter total file required:")

content = """Email: Rahul.Shinde@gmail.com
Firstname : Harish
Lastname : rathod
Email: Harish.rathod@gmail.com
"""
for i in range(int(user_input)):
    with open("file"+str(i)+".txt", 'w+')as f:
        f.write(content)