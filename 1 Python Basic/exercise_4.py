# Exercise 4. String Slicing and Substring Removal

def remove_chars(word, n):
    print('Original string:', word)
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("buildscript", 4))
print(remove_chars("uchihamadara", 2))