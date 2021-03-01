# !/bin/python3
# lyrics.py
# Author: Advik Singhania
# Date: 12th February, 2021
'''Song-Lyrics-Fetcher'''
'''A Python3 script to fetch the lyrics of a song using Genius API and lyricsgenius module.'''

# Importing the required modules:
try:
    import os
    import lyricsgenius as lg
except ModuleNotFoundError:  # Handle the error if the module is not found
    print(
        'Module not found. Run "python3 -m pip install lyricsgenius" to install it.'
    )

# Creating an instance of the Genius API and giving it the required API Token
# Replace Insert_Client_API_Token_Here with your API Token
genius = lg.Genius('Insert_Client_API_Token_Here',
                   skip_non_songs=True,
                   excluded_terms=["(Remix)", "(Live)"],
                   remove_section_headers=True)

# Taking the title name of the song and the artist name as the input from the user:
title = input('Enter the title of the song   : ')
artist = input('Enter name of the artist/band : ')

print()  # Empty line

# Creating a file to store the lyrics:
# filename for the file is the name of song
filename = '-'.join((title + ' ' + artist).split()) + '-lyrics.txt'

if os.path.exists(filename):  # If the file already exists
    print('Lyrics of "' + title + '" already saved to the file', filename)
    exit()  # Then print the name of the file and exit
else:
    # Opening the file with filename in writing mode
    file = open(filename, 'w')
    try:
        song = genius.search_song(title, artist)  # Searching for the song
        file.write(song.lyrics)  # Writing the lyrics of the song to the file
        print('Lyrics of "' + title + '"', 'found and saved to the file',
              filename)
        file.close()  # Closing the file upon writing the contents successfully
    except:
        file.close()
        os.remove(filename)  # Deleting the file if no lyrics are found
        print('Error finding the lyrics of the song "' + title + '" by',
              artist)  # Print an error if the lyrics are not found
