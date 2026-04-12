# Exercise 13. Currency formatting with commas

amount = float(input("Please enter the amount of dollars: "))
formatted_amount = f"{amount:,.2f}"
print(f"Total Balance: ${formatted_amount}")