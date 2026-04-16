# Exercise 7 -
from cleo.io.outputs import output

with open("output.txt", "w") as f:
    f.write("Hello, BuildScript!\n")

with open("output.txt", "r") as f:
    data = f.read()
    print(data)