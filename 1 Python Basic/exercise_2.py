# Exercise 2. Cumulative Sum of a Range

num = int(input("Enter a number: "))
print(f"Printing current and previous number sum in a range({num})")
prev = 0
for i in range(num):
    x_sum = prev + i
    print(f"Current Number {i} Previous Number {prev} Sum: {x_sum}")

    prev = i
