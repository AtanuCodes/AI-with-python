# collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string

def generate_password(length, use_uppercase, use_special, use_digits):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special:
        characters += string.punctuation
    if use_digits:
        characters += string.digits
    
    password = []
    
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_special:
        password.append(random.choice(string.punctuation))
    if use_digits:
        password.append(random.choice(string.digits))
    
    while len(password) < length:
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    return ''.join(password)

length = int(input("Enter the desired password length: "))
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'

try:
    password = generate_password(length, use_uppercase, use_special, use_digits)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(e)
