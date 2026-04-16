# Exercise 4: Count Words From a File

def filename(name):

    # f = open(f"{name}", "w")

    with open(f"{name}", 'r') as f:
        data = f.read().split()
        count = 0


        for word in data:
            count += 1

        print(f"Total Number of words present in file is {count}")

filename("WordCounter.txt")