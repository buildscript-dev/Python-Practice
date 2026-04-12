# Exercise 15. Tabular output from lists

names = input("Enter all names: ").capitalize()
namelst = list(map(str, names.replace(",", " ").split()))

scores = input("Enter all scores: ")
scoreslst = list(map(int, scores.replace(",", " ").split()))

title = f"{"Name":<10}" "Score"
print(title)
dash = "-" * len(title)
print(dash)

for name, score in zip(namelst, scoreslst):
    print(f"{name:<10}{score}")