# Exercise 2. Create a string made of the middle three characters

txt = input("Enter any text: ")
mid_txt = len(txt)//2
txt_format = txt[mid_txt - 1] + txt[mid_txt] + txt[mid_txt + 1]
print(txt_format)
