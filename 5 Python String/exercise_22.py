# Exercise 22. Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

filtered_list = list(filter(None, str_list))

print(filtered_list)