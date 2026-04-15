# Exercise 8. Generate a List of Even Numbers (Range Function)

def even_num(num):
    lst = []
    for i in range(1, num+1):
        if i % 2 == 0:
            lst.append(i)
    print(lst)
result = even_num(20)

# print(result)