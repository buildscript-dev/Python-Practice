# Exercise 19. Armstrong Number Check

number = input("Enter a number: ")
digit = len(number)

armstrong = 0
for i in number:
    armstrong += int(i) ** digit

if armstrong == int(number):
    print(f"The number {number} is an armstrong number")
else:
    print(f"The number {number} is not an armstrong number")

