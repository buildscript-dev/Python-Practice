# Exercise 4. Create a new string made of the first, middle, and last characters of each input string

s1 = "America"
s2 = "Japan"

# Get first, middle and last character from first string
first_char = s1[0]
middle_char = s1[int(len(s1) / 2)]
last_char = s1[-1]

# Get first, middle and last character from second string
first_char2 = s2[0]
middle_char2 = s2[int(len(s2) / 2)]
last_char2 = s2[-1]

# Combine all
res = first_char + first_char2 + middle_char + middle_char2 + last_char + last_char2
print("New String:", res)