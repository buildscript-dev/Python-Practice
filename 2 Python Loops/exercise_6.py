# Exercise 6. Calculate the cube of all numbers from 1 to a given number

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(f"The cube of {i} is {i**3}")
