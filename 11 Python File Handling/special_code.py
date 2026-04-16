import os

base_name = "exercise"
count = int(input("Enter number of files you need: "))

# get current script folder
folder = os.path.dirname(os.path.abspath(__file__))

for i in range(1, count + 1):
    filename = os.path.join(folder, f"{base_name}_{i}.py")

    with open(filename, "w") as f:
        f.write(f"# Exercise {i} - ")

print("Files created successfully")