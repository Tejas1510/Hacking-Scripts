# !/bin/python3
# e-dictionary.py
# Author : Advik Singhania
# NOTE: Requires internet connection. see README.md for more information.
'''A Python script that gives the meaning, synonyms and antonyms of a word using PyDictionary'''

try:  # Check and import if the module for dictionary is installed or not
    from PyDictionary import PyDictionary
except ModuleNotFoundError:
    print('PyDictionary package is not installed.')
    print("Run 'pip install PyDictionary' on your terminal to install it.")
    exit()


def find_meaning(word):  # Function to find the meaning of the word
    try:
        mean = dict.meaning(word)
        mean_keys = mean.keys()
    except AttributeError:  # If the word is not in the dictionary, print error and exit
        print('Word not found in Dictionary')
        exit()

    for i in mean_keys:  # For different keys in the dict(mean), print the key
        print('(', i, ')', sep='')  # e.g.: Noun, Verb, Adjective
        for j in range(len(mean[i])):  # and print the data for that respective key, line by line
            print('\t', j+1, '. ', mean[i][j], sep='')
        print()


def find_synonyms(word):  # Function to find the synonyms of the word
    syn = dict.synonym(word)  # list containing the synonyms
    print('(Synonyms)\n\t', end='')
    for i in syn:
        print(i, end=', ')
    print('\n')


def find_antonyms(word):  # Function to find the antonyms of the word
    ant = dict.antonym(word)  # list containing the antonyms
    print('(Antonyms)\n\t', end='')
    for i in ant:
        print(i, end=', ')
    print('\n')


dict = PyDictionary()  # Creating an instance of the module
word = input('Enter a word: ')
print()
find_meaning(word)
find_synonyms(word)
find_antonyms(word)
