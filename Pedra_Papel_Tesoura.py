import random

def get_user_choice():
    """
    Ask the user for a valid choice.
    """
    while True:
        choice = input("Choose rock, paper or scissors (or 'exit' to quit): ").lower()

        if choice == "exit":
            return None

        if choice in ["rock", "paper", "scissors"]:
            return choice

        print("Invalid choice! Try again.")


def get_computer_choice():
    """
    Generate a random choice for the computer.
    """
    options = ["rock", "paper", "scissors"]
    return random.choice(options)


def determine_winner(user, computer):
    """
    Determine the winner of the round.
    """
    if user == computer:
        return "draw"

    if (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"

    return "computer"


def show_result(user, computer, result):
    """
    Display the result of the round.
    """
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")


def main():
    """
    Main game loop.
    """
    print("=== Rock, Paper, Scissors ===")

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        show_result(user_choice, computer_choice, result)


if __name__ == "__main__":
    main()