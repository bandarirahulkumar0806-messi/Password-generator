import random
import string

# Prompt user for password length
length = int(input("Enter the desired length of the password: "))

# Define characters to use (letters, digits, punctuation)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)
