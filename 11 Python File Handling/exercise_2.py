# Exercise 2: Read File Line by Line

with open('sample.txt', 'r') as file:
    for line in file:
        print(line, end="")