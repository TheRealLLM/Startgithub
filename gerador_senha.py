import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    # Ask user for password length
    user_length = input("Enter the desired password length: ")
    if user_length.isdigit():
        user_length = int(user_length)
    else:
        print("Invalid input! Exiting...")
        quit()

    # Ask user which character types to include
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    # Generate password
    password = generate_password(user_length, use_upper, use_lower, use_numbers, use_symbols)

    # Show password
    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    main()