# Calculate the factorial of a number

number = int(input("Enter your number: "))

factorial = 1

for num in range(1, number + 1):
    factorial *= num

print(factorial)
