import re

password = input("Enter password to check strength: ")


def password_check(password):
    """
    This function verifys the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if it contains:
        at least 8 characters long
        at least 1 number,
        at least 1 symbol,
        at least 1 uppercase letter,
        at least 1 lowercase letter.
    """

    # calculating the length
    length_check = len(password) < 8

    # searching for number
    num_check = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_check = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_check = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_check = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
                             password) is None

    # overall result
    strong = not (length_check or num_check or uppercase_check
                  or lowercase_check or symbol_check)

    return {
        'Password is Strong': strong,
        'Password is short': length_check,
        'Password does not have number': num_check,
        'Password does not use uppercase alphabets': uppercase_check,
        'Password does not use lowecase alphabets': lowercase_check,
        'Password does not contain special character': symbol_check,
    }


dict = password_check(password)

for statement, condition in dict.items():
    if condition:
        print(statement)
