import random

def choose_difficulty():
    """
    Ask the user to choose a difficulty level.
    Returns the max number and attempts allowed.
    """
    print("Choose difficulty:")
    print("1 - Easy (1 to 10, 4 attempts)")
    print("2 - Medium (1 to 50, 7 attempts)")
    print("3 - Hard (1 to 100, 10 attempts)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 10, 4
    elif choice == "2":
        return 50, 7
    elif choice == "3":
        return 100, 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10, 4

def generate_secret_number(max_value):
    """
    Generate a random number based on difficulty.
    """
    return random.randint(1, max_value)

def get_user_guess(max_value):
    """
    Get a valid number from the user.
    """
    guess = input(f"Enter a number between 1 and {max_value}: ")

    if not guess.isdigit():
        print("Invalid input. Please enter numbers only.")
        return None

    return int(guess)

def check_guess(guess, secret_number):
    """
    Compare the guess with the secret number.
    """
    if guess < secret_number:
        print("Too low!")
        return False
    elif guess > secret_number:
        print("Too high!")
        return False
    else:
        print("🎉 Congratulations! You guessed it!")
        return True

def play_game():
    """
    Main game logic.
    """
    max_value, attempts_left = choose_difficulty()
    secret_number = generate_secret_number(max_value)

    print("\nGame started!")

    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")

        guess = get_user_guess(max_value)

        if guess is None:
            continue

        if check_guess(guess, secret_number):
            return

        attempts_left -= 1

    print(f"\n❌ Game over! The number was {secret_number}")

def play_again():
    """
    Ask the user if they want to play again.
    """
    choice = input("\nDo you want to play again? (y/n): ").lower()

    return choice == "y"

def main():
    """
    Main program loop.
    """
    while True:
        play_game()

        if not play_again():
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()