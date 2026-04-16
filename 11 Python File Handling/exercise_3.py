# Exercise 3: Read Specific Lines From a File

count = 0

with open('sample.txt', 'r') as f:
    for i in f:
        print(i, end="")
        count += 1

        if count == 4:
            break
