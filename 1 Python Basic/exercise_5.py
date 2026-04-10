# Exercise 5. Variable Swapping (The In-Place Method)

a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")
a = a+b
b = a-b
a = a-b
print(f"After Swap : a = {a}, b = {b}")