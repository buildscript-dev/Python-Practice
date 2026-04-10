# Exercise 4. Calculate the sum of all numbers from 1 to N

num = int(input("Enter a number: "))
sum = 0

for i in range(num+1):
    sum += i
print(f"The sum is {sum}")