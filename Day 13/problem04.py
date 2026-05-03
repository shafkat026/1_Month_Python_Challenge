# Mini Password Generator 

# Generate a random password based on user requirements:

# Length of password
# Include uppercase? (Y/N)
# Include numbers? (Y/N)
# Include symbols? (Y/N)

# 💡 Hint:

# Use random module (random.choice, random.shuffle)
# Use string module:
# string.ascii_letters, string.digits, string.punctuation

import random
import string

length = int(input("Enter Length:"))
UpC = str(input("Include Uppercase? (Y/N):").lower())
Num = str(input("Include Number? (Y/N):").lower())
Sym = str(input("Include Symble? (Y/N):").lower())


chars = string.ascii_lowercase

if UpC == "y":
    chars += string.ascii_uppercase
if Num == "y":
    chars += string.digits
if Sym == "y":
    chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
# _ means “I don’t care about the variable”

print("Password:", password)