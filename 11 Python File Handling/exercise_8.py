# Exercise 8: Append To a File

with open("output.txt", "a") as f:
    f.write("AI Engineer and Problem Solver....")

with open("output.txt", "r") as f:
    data = f.read()
    print(data)