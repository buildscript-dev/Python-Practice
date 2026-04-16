# Exercise 5: Count Total Number of Characters in File

with open('WordCounter.txt', 'r') as f:
    data = f.read()
    print(len(data))


