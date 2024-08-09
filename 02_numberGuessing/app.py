from random import randint

lower_number, upper_number = 1, 10
random_number: int = randint(lower_number, upper_number)

print(f"Guess then number between {lower_number} and {upper_number}: ")

while True:
    try:
        user_guess: int = int(input("Guess:"))
    except ValueError as e:
        print("Please enter a valid number.")
        continue

    if user_guess > random_number:
        print("The number is lower")
    elif user_guess < random_number:
        print("The number is higher")
    else:
        print("You guessed it!")
        break
