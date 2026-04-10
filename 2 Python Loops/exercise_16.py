# Exercise 16. Check if a number is a palindrome

number = int(input("Enter a number: "))
rever = ""

for i in str(number):
    rever = i + rever

rever = int(rever)
if number == rever:
    print(f"This is Palindrome Number: {rever}")
else:
    print(f"This is Not Palindrome Number: {rever}")
