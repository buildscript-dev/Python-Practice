# Exercise 12. Count vowels and consonants in a sentence

user_input = input("Enter a sentence: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0
count_consonants = 0

for char in user_input:
    if char.isalpha():   # ignore spaces/symbols
        if char in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print(f"Total vowels: {count_vowels}")
print(f"Total consonants: {count_consonants}")