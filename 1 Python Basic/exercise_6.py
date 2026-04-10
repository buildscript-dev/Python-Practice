# Exercise 6. Calculating Factorial with a Loop


user_input = int(input("Enter a number: "))
factorial = 1

for i in range(1, user_input + 1):
    factorial *= i

print(factorial)
