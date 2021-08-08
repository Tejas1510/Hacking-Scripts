import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()

digits = "0123456789"
symbols = "@#$%^&*(){}[]./\?-_"

upper = True
lower = True
numbers = True
special_char = False

all_chars = ""

if upper:
    all_chars += uppercase_letters
if lower:
    all_chars += lowercase_letters
if numbers:
    all_chars += digits
if special_char:
    all_chars += symbols

pass_length = 15
no_of_passwords = 10

for i in range(no_of_passwords):
    password = "".join(random.sample(all_chars, pass_length))
    print(password)
