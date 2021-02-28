# !/bin/python3
# script.py
# Author: Advik Singhania
# Date: 8th Jan, 2021
'''Caesar-Cipher'''
'''A Python script to encrypt or decrypt text according to a shift value'''


def encrypt(s):  # Function for encrypting the text
    print('\n[#] Encrypted text output :', end=' ')
    for x in s:  # Repeating the loop for each character in the string
        if x.isalpha():  # Check if the chracter is an alphabet (irrespective of the case)
            # If True, then process the ASCII value of the shifted character
            var = ord(x)
            var += n
            if var > 90:
                var -= 26

            if var < 65:
                var += 26

            print(chr(var), end='')  # And print the shifted character
        else:
            print(x, end='')  # Else print the character as it is

    print('\n')


def decrypt(s):  # Function for decrypting the text
    print('\n[#] Decrypted text output :', end=' ')
    for x in s:  # Repeating the loop for each character in the string
        if x.isalpha():  # Check if the chracter is an alphabet (irrespective of the case)
            # If True, then process the ASCII value of the shifted character
            var = ord(x)
            var -= n
            if var > 90:
                var -= 26

            if var < 65:
                var += 26

            print(chr(var), end='')  # And print the shifted character
        else:
            print(x, end='')  # Else print the character as it is

    print('\n')


print('\n\tCaeser Cipher Encrypter/Decrypter')
while True:  # Running as long as the user wants
    try:
        print('[+] Options :\n\t1.) Encrypt Text\n\t2.) Decrypt Text')
        print('\tPress Ctrl+C to exit.')
        try:
            # Taking choice as the input
            ch = int(input('[+] Enter your choice (1/2) : '))
        # If the input is not an integer (1 or 2), run the loop again
        except ValueError:
            print('[!] Invalid input. Try again.\n')
            continue

        if ch == 1:
            text = input('[+] Input text : ')  # Input string/text
            text = text.upper()  # Converting the text to uppercase
            try:
                # Input shift value for encryption
                n = int(input('[+] Enter offset : '))
                # Shift should be in the range of [-26,26]
                if n >= 26 or n <= -26:
                    print('[!] Invalid Input. Enter a number between -25 to 25\n')
                else:
                    encrypt(text)  # Calling the encryption function

            except ValueError:  # If the shift value is not an integer, throw error
                print('[!] Invalid Input.\n')

        elif ch == 2:
            text = input('[+] Input text : ')  # Input string/text
            text = text.upper()  # Converting the text to uppercase
            try:
                # Input shift value for decryption
                n = int(input('[+] Enter offset : '))
                # Shift should be in the range of [-26,26]
                if n >= 26 or n <= -26:
                    print('[!] Invalid Input. Enter a number between -25 to 25\n')
                else:
                    decrypt(text)  # Calling the decryption function

            except ValueError:  # If the shift value is not an integer, throw error
                print('[!] Invalid Input.\n')

        else:
            print('[!] Invalid choice.\n')

    except (EOFError, KeyboardInterrupt):  # If the user presses Ctrl+C (keyboard interruption)
        print('\n[!] Exiting...')  # Exit the loop
        break

# Exiting the program
exit()
