# Song-Lyrics-Fetcher

## Introduction
A Python3 script that takes the title of the song and the name of the artist or the band as the input and outputs the lyrics for that song.

## Third-party Libraries Required :
This script uses the [lyricsgenius](https://github.com/johnwmillr/LyricsGenius) module which makes use of the [Genius](https://genius.com/Genius-about-genius-annotated) and its [API](https://docs.genius.com/) to fetch the lyrics of the song.

## How to install the above Library
*   Run the following command on your terminal to install the library for Python.
    ```bash
    $ python3 -m pip install lyricsgenius
    ```
*   Setting up the API Client
    -   Review the  [API documentation page](https://docs.genius.com/).
    -   Review the  [API Terms of Service](https://genius.com/static/terms).
    -   From the documentation page, click  _API Client management page_  to navigate to the  [Sign-up/Log-in page](https://genius.com/signup_or_login).
    -   Complete the form using the signup, or login (if you have an account), method of your choice and click  _Create Account_. This should take you to your  _API Clients_  page or re-route you back to the home page. If you are sent back to the home page, scroll down to the page footer and click  _Developers_.
    -   Once on the API Clients page click _Create an API Client_ (on Safari) or _New API Client_ (on Chrome) to create your app. In this context, the term “app” refers to usage of the Genius API. Only the _App Name_ and _App Website URL_ fields are necessary to progress. The app name will chiefly be used by us to identify this individual client (you can create several API clients). I typically default to using my Github for most website requirements but any site should be fine for the URL field.
    -   Clicking _Save_ will take you to the credentials page. If you’ve created multiple API clients, they’ll all show up here.
    -   On your API Clients page, click on Generate Access Token. This token will be passed to lyricsgenius.Genius() along with the parameters we want to use to filter the text data.

## How to use it:

*   Download and install the latest version of [Python](https://www.python.org).
*   Download and save the script.
*   Navigate to the directory where you have saved it and open the script in an editor.
*   Replace the `Insert_Client_API_Token_Here` with your API Token generated for your account.
*   Run `python lyrics.py` in a terminal or `python3 lyrics.py` if you have Python 2 installed as well.
*   Enter the title of the song you want the lyrics for.
*   Enter the name of the artist/album/band whose song it is.
*   The lyrics will be saved to a text file with the name as title-artist-lyrics.txt
*   NOTE: The script will show error and exit, if no lyrics for the song is found.

## Output
#### Input Images

<img src="https://github.com/adviksinghania/Hacking-Scripts/raw/patch-lyrics-fetcher/Python/Song-Lyrics-Fetcher/input.jpg">

#### Output Images

<img src="https://github.com/adviksinghania/Hacking-Scripts/raw/patch-lyrics-fetcher/Python/Song-Lyrics-Fetcher/output1.png">
<img src="https://github.com/adviksinghania/Hacking-Scripts/raw/patch-lyrics-fetcher/Python/Song-Lyrics-Fetcher/output2.png">

<br><br>

![built by developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)
![built with love](https://forthebadge.com/images/badges/built-with-love.svg)
![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)

Check out my Github profile: [Advik Singhania](https://github.com/adviksinghania)!
