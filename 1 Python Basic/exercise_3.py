# Exercise 3. String Indexing and Even Slicing
from subprocess import check_output

txt = input("Original String is ")
print("Printing only even index chars")
count = 0
for i in range(0, len(txt), 2):
    print(txt[i])