# Exercise 16. Interactive menu


while True:
    choice = int(input("Enter choice(1-3): "))

    if choice == 1:
      print("Hello, Build")
    elif choice == 2:
        square = int(input("Enter a number: "))
        print(square ** 2)
    elif choice == 3:
        print("Bye Bye..., Build")
        break
    else:
        print("Please enter a valid choice")
