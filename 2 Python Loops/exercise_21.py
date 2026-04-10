# Exercise 21. Print the decreasing pattern

print("Number Pattern:")

for i in range(6, 0, -1):   # step = -1
    for j in range(1, i + 1):
        print(i, end=' ')
    print()
