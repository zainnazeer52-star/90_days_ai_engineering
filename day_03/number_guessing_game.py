
secret_number = 7
attempts = 3

while attempts > 0:
    guess = int(input("Enter a number between 1 and 10: "))

    if guess < 1 or guess > 10:
        print("Please enter a valid number between 1 and 10.")
        continue

    attempts = attempts - 1

    if guess > secret_number:
        print("Your guess is too high.")

    elif guess < secret_number:
        print("Your guess is too low.")

    else:
        print("Congratulations! You guessed the secret number.")
        break

    print(f"Remaining attempts: {attempts}")

else:
    print("Game over!")
    print(f"The correct number was: {secret_number}")
