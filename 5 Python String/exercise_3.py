# Exercise 3. Append new string in the middle of a given string

oldStr = input("Enter a string")
newStr = input("Enter new string: ")
old_format = len(oldStr)//2
left_str = oldStr[:old_format]
center_str = newStr
right_str = oldStr[old_format:]

print(left_str + center_str + right_str)