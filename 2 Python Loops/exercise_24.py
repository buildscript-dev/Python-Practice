# Exercise 24 - Hollow square pattern
from timeit import repeat

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        # print star on borders only
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()