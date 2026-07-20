# Ask the user for a number and calculate the sum from 1 to that number.

user_number = int(input("Enter your number: "))

total = 0

for value in range(1, user_number + 1):
    total = total + value
    print("Total", total)
