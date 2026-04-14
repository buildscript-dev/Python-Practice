# Exercise 17. Lowercase First

user_input =input("Enter any String: ")
lower_string=""
upper_string=""
for i in user_input:
    if i.islower():
        lower_string += i
    elif i.isupper():
        upper_string += i
print(lower_string + upper_string)
