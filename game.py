import random


def guessing_game():
    secret_number = random.randint(1, 100)

    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        user_guess = int(input("Enter your guess: "))

        attempts += 1

        if user_guess == secret_number:
            print(f" Congratulations! You guessed it in {attempts} attempts.")
            break

        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")


if __name__ == "__main__":
    guessing_game()
