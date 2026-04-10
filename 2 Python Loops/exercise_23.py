# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern

user_input = input("Enter a letter: ").upper()
for i in range(ord("A"), ord("Z") + 1):
    for j in range(ord("A"), i + 1):
        print(chr(i), end=" ")

    if chr(i) == user_input:
        break
    print("")