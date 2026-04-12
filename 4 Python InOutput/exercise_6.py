# Exercise 6. Hexadecimal representation

num = int(input("Enter a number: "))

# :x produces lowercase (ff), :X produces uppercase (FF)
hex_val = f"{num:x}"

print(f"The hexadecimal value is {hex_val}")
