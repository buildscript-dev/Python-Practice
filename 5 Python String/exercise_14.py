# Exercise 14 -


string = "Hello, Build"
nth = int(input("Enter the index value: "))

first_part = string[:nth]
second_part = string[nth + 1:]
result = first_part + second_part

print(result)