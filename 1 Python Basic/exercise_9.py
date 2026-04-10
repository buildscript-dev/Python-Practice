# Exercise 9. Vowel Frequency Counter

sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(f"Total number of vowels: {count}")

