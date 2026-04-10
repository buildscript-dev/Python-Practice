# Exercise 11. Reverse a string using a for loop (no slicing)

user_input = input("Original: ")
rever = ""
for char in user_input:
    rever = char + rever

print(rever)