number = int(input("Enter a number: "))

print(f"Multiplication table of {number}")

for value in range(1, 11):
    result = number * value
    print(f"{number} * {value} = {result}")
