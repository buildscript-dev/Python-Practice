
base_name = "exercise"
count = int(input("Enter number of files you need: ")) # number of files

for i in range(1, count + 1):
    filename = f"{base_name}_{i}.py"

    with open(filename, "w") as f:
        f.write(f"# Exercise {i} - ")

print("Files created successfully")