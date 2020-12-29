import string
import secrets

print("We reccomend using password that is more than 8 character long")

n = int(input("Enter password length: "))

special_chars = "!#$%-_=+$&@!: "
def isspecial(char):
    if char in special_chars:
        return True
    return False
def password_generator(n):
    if n < 6:
        return "Password you are trying to generate is to short"
    char_set = string.ascii_letters + string.digits + special_chars
    while True:
        password = ''.join(secrets.choice(char_set) for i in range(n))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(isspecial(c) for c in password)):
            return password
print(password_generator(n))