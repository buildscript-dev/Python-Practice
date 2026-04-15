# Exercise 5. Create an Inner Function


def outer_fun(a,b):
    def inner_fun(a,b):
        return a+b
    return inner_fun(a,b) + 5

result = outer_fun(10, 5)
print(result)