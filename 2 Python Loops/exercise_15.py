# Exercise 15. Find largest and smallest digit in a number

number = int(input("Enter a number: "))
largest = 0
smallest = largest

for i in number:
    if i >= largest:
        largest = i

    if i <= smallest:
        smallest = i

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")