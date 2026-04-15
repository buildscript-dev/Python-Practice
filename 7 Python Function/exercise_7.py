# Exercise 7. Assign a Different Name to Function and Call It

def display_student(name, rollNum):
    rollNum = str(rollNum)

    if len(rollNum) == 1:
        rollNum = "0" + rollNum
    print("Hey, {} your roll no. is {}".format(name, rollNum))


def show_student(name, rollNum):
    display_student(name, rollNum)


show_student("Build", 77)