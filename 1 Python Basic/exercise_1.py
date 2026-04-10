# Exercise 1. Arithmetic Product and Conditional Logic

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = num1 + num2
    prod = num1 * num2

    if prod <= 1000:
        print("The Product is", prod)
    else:
        print("The Sum is", total)

except ValueError:
    print("Please check your input")