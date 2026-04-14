# Exercise 1. Create a string made of the first, middle, and last character

name = "Build"
name_formatting = name[0].upper() + name[len(name)//2] + name[-1]

print(name_formatting)