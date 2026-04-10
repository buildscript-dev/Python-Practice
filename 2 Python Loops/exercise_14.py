# Exercise 14. Reverse an integer number

number = 1234567890
rever = ""

for char in str(number):
    rever = char + rever


rever = int(rever)
print(rever)
