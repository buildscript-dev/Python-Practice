# Exercise 9. Find the Largest Item in a List

lst = [4, 6, 8, 24, 12, 2]

# 1st Method:

# largest = max(lst)
# print(largest)


# 2nd Method:

largest = 0

for i in lst:
    if i > largest:
        largest = i

print(largest)