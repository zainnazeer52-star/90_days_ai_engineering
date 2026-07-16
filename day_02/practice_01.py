# Ask the user for a number and determine whether it is positive, negative, or zero.

number = float(input("Enter your number: "))

if number < 0:
    print("Number is negative. ")

elif number > 0:
    print("Number is positive. ")

else:
    print("Number is zero. ")
