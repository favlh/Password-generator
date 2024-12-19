import random
import string

def password_generator(length=12):
    # Characters used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random and complex password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = int(input("Enter the desired password length: "))  # Prompt the user to enter password length
for _ in range(10):
    print(password_generator(password_length))  # Generate a password of the specified length
