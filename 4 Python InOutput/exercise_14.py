# Exercise 14: Accept a list of 5 float numbers



number = input("Enter a number: ")
value = list(map(float, number.replace(",", " ").split(" ")))
print(value)
