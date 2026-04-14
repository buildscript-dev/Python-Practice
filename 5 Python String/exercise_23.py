# Exercise 23. Remove special symbols/punctuation from a string

string = "/*Jon is @developer & musician!!"


for char in string:
    if char.isalnum():
        print(char, end= "")
    elif char.isspace():
        print("",end=" ")
    else:
        continue

