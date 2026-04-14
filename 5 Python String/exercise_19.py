# Exercise 19. Create a mixed string using alternating characters

s1 = "Abc"
s2 = "Xyz"
s3 = ""

s2 = s2[::-1]

for i in range(len(s1)):
    s3 += s1[i] + s2[i]

print(s3)