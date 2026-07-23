def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("number can't divided by 0")
    else:
        return (a / b)


number_one = float(input("Enter you first number: "))
number_two = float(input("Enter your second number: "))
choice = (input("Select the operation: +, -, *, / "))

if choice == "+":
    print("Addition: ", add(number_one, number_two))
elif choice == "-":
    print("Substraction: ", sub(number_one, number_two))
elif choice == "*":
    print("Multiplication: ", multiply(number_one, number_two))
elif choice == "/":
    print("Division: ", divide(number_one, number_two))
else:
    print("please choose a valid operator.")
