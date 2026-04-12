# Exercise 26 - Print full multiplication table (1 to 10)

for i in range(1, 11):
    for j in range(1, 11):
        # print(f"{i} x {j} = {i*j}")
        print(f"{i*j}" , end="  ")
        if j == 10:
            print(" ", end="\n")

