input_str="Hello CoronaHowAreYou,please go away"
input_word="CoronaHowAreYou"
dict={ }
for str in input_word:
    print (str)
    if str in dict:
        dict[str] +=1
    else:
        dict[str]=1
        print ("result:",dict)