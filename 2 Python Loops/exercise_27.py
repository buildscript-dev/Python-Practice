# Exercise 27 - List Cumulative Sum: Each element is the sum of all previous

prev = 0
for i in range(1, 10):
    prev += i
    print(prev, end=" ")