# Exercise 18. Count all letters, digits, and special symbols from a given string


strings = "P@#yn26at^&i5ve"

letter = 0
digit = 0
symbol = 0

for i in strings:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i == " " or i == "":
        continue
    else:
        symbol += 1

print("Total counts of chars, digits, and symbols: Chars = {} Digits = {} Symbol = {}".format(letter, digit, symbol))


