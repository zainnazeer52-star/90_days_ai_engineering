# Ask the user for five numbers and calculate the total.

total = 0

for count in range(1, 6):
    number = float(input(f"Enter number {count}: "))
    total = total + number

print("Total:", total)
