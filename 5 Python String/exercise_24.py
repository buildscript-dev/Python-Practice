# Exercise 24. Remove all characters from a string except integers

string = "I am 25 years and 10 months old"


for num in string:
    if num.isnumeric():
        print(num, end="")



