import random
import string

def generate_password(length):
    # Define the characters we can use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters and join them into a password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for desired password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Your new password is: {password}")
