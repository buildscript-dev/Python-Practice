# Exercise 17. Masked password input (getpass)
import getpass

print("Welcome, Admin")

password = getpass.getpass("Password: ")

if password == "12345":
    print("Ooh, Welcome Beautiful")
    print("Wanna go on Date...")
else:
    print("Access denied")
    print("Please try again")