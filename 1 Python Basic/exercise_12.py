# Exercise 12. List Comparison and Boolean Logic

num_x = [10, 20, 30, 40, 10]
num_y = [75, 65, 35, 75, 30]

def checker(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False

num = checker(num_y)
print(num)