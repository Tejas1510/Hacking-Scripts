import string
import secrets
"""
    This is random password generator which creates
    random password using "secrets" module.
    Since secret module uses systems CSPRNG
    therefor each charecter of password provides 6.169 bits
    of entropy.
"""

print("We reccomend using password that is more than 8 character long")

n = input("Enter password length (Default = 16): ") or 16
n = int(n)

# Checkes if char is special charecter.
special_chars = "!@#$%^&*()"


def isspecial(char):
    if char in special_chars:
        return True
    return False


# Generates password using secrets module.


def password_generator(n):
    if n < 6:
        return "Password you are trying to generate is to short"
    char_set = string.ascii_letters + string.digits + special_chars

    # Generates password till password satisfies all standerd conditions.
    while True:
        password = ''.join(secrets.choice(char_set) for i in range(n))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password)
                and any(c.isdigit() for c in password)
                and any(isspecial(c) for c in password)):
            return password


print(password_generator(n))
