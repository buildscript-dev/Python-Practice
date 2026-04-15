# Exercise 2. Variable Length of Arguments (*args)

def func1(*num):
    print("Printing Values:")
    for i in num:
        print(i)

func1(10, 20, 30)
func1(100, 90, )