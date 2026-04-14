# Exercise 20. Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
sum = 0
count = 0
for i in str1:

    if i.isdigit():
        i = int(i)
        sum += i
        count += 1

average = sum / count
print(f"Sum is: {sum}, Average is: {"%.2f" % average}")