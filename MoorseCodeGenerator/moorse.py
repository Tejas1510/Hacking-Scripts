import encrypt
import decrypt

# here i have used the standard moorse code chart provided by wikipedia and other website
# I have also added a photo in readme which you can check for better understanding
moorsecode = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

if __name__ == "__main__":
    while True:
        print('\nHello welcome to Tejas Moorse Code translator')
        print('press 1 for English to Moorse Code Converter : ')
        print('press 2 for Moorse code to English Converter : ')
        print('press 3 to exit')
        x = input('')
        if x == '1':
            z = input('Enter the text you want to convert to morse code:')
            e_msg = encrypt.encrypt(z, moorsecode)
            e_string = ""
            for i in e_msg:
                e_string = e_string + i + "/ "
            e_string = e_string[:-2]
            print('encrypted code:' + e_string)
        elif x == '2':
            z = input('Enter the Moorse Code to convert to english:')
            d_msg = decrypt.decrypt(z, moorsecode)
            d_string = ""
            for i in d_msg:
                d_string = d_string + i + ' '
            d_string = d_string[:-1]
            print(d_string)
        elif x == '3':
            exit(True)
        else:
            print('invalid input')
            continue
