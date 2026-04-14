# Exercise 10. Vowel Counter

vowels = "aeiou"
count = 0
string = "BuildScript"
for char in string:
    if char in vowels:
        count += 1
    else:
        continue

print("Total number of vowels:", count)

