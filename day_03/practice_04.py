# Ask the user for a word and count how many letters it contains.

word = input("Enter you word here: ")

letter_count = 0

for letter in word:
    letter_count = letter_count + 1

print("Total Count", letter_count)
