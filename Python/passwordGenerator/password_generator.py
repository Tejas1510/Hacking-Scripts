import _sha512
from getpass import getpass
import string

"""
    This password generator takes length of
    password, username, service name and a secret key.
    
    It uses sha512 to generate password from credentials.
"""


# Change it to increase maximum length that can be generated.
# Since sha512 can generate 64 8bit values MAX_LEN can not go beyond that.
# It is recommended to not increase it beyond 50.
MAX_LEN = 32

n = input("Enter length of password: ") or 16
n = int(n)
username = input("Enter username: ")
service = input("Enter service name (example.com): ")

# getpass function does not show input when typed.
secret = getpass("Enter secret key (Not show as you type) : ")

credentials = username + service + service + str(n)

# A function to check for spacial charecters
# since i was unable to find inbuit.
def isspecial(char):
    if char in string.punctuation:
        return True
    return False

# Our main function to generate password.
def password_generator(credentials, n):
    
    # Generates sha512 hash
    hash = _sha512.sha512(credentials.encode()).hexdigest()

    lst = []
    
    # Pairs every two hexadecimal numbers.
    # Discards values greater than 196 and normalizes
    # remaining values in range 32 to 128 for
    # easy conversation to ascii.
    # Saves values in lst.  
    for i in range(0,128,2):
        j =  int(hash[i]+hash[i+1], 16)
        if 96 <= j < 192:
            lst.append(j - 66)
        elif j < 96:
            lst.append(j+30)
        
    # If number of usable values is less than needed
    # then start again with hash as new credentials.
    # If false output list will have charecters insted of numbers.
    if (len(lst) < n):
        lst = password_generator(hash, n)
    
    # Converts integers in list to their ASCII eqvivalant
    # and discards values after 'n' index.
    if type(lst[0]) != str:
        for i in range(n):
            lst[i] = str(chr(lst[i]))
        lst = lst[:n]

    # Checks if password have upeercase, lowercase,
    # digit and special charecters.
    # If any is missing start again with hash as new input.
    if not (any(c.islower() for c in lst)
                and any(c.isupper() for c in lst)
                and any(c.isdigit() for c in lst)
                and any(isspecial(c) for c in lst)):
        lst = password_generator(hash, n)

    return lst

if n <= MAX_LEN:
    lst = password_generator(credentials, n)
    print("\nPassword is:- ")
    for i in lst:
        print(i, end="")
    print()

else:
    print("Password longer than we can generate maximum length is 32")