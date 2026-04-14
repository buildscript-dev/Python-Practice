# Exercise 21. Count occurrences of all characters within a string

str1 = "apple"
char_dict = dict()

for char in str1:
    if char in char_dict:
        char_dict[char] += 1
    else:
        # Add the character to the dictionary
        char_dict[char] = 1

print(char_dict)
