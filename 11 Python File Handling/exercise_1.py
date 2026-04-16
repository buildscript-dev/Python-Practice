# Exercise 1: Read a File

# f = open("sample.txt", 'x')

with open("sample.txt", "r") as f:
    # single_line_data = f.readline()
    # print(single_line_data)

    double_line_data = f.read()
    print(double_line_data)