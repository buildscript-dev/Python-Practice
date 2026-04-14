# Exercise 25. Find words with both letters and numbers

string = "Emma25 is Data scientist50 and AI Expert"
list_string = list(string.split())

print("Original:", list_string)
for words in list_string:
    if any(char.isalpha() for char in words) and any(char.isdigit() for char in words):
        print(words)

