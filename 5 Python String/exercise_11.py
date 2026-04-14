# Exercise 11. Prefix/Suffix Check

string = "https://google.com".lower()
prefix = string.startswith("https://")
suffix = string.endswith(".com")

if prefix:
    print("Fetching the data....")
    if suffix:
        print("You can access....")
    else:
        print("Sorry... We need .com")
else:
    print("We need https for secure internet....")