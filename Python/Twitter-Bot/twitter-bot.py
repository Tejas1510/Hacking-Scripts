from re import search
import tweepy
import time
from tweepy.api import API
import requests
import json

from tweepy.models import Status

auth = tweepy.OAuthHandler('*****enter API key here*****','*****enter secret API key*****')

auth.set_access_token('*****enter access token*****','*****enter secret access token*****')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()
    
nrTweets = 1       

search = 'Basketball', 'good'
nrTweets = 5

# Crawl tweets and like tweets that have specific keywords in them
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print (e.reason)
    except StopIteration:
        break

# calling an api and tweeting the response 
def getQuote():
    url = "https://animechan.vercel.app/api/random"

    response = requests.get(url)
            
    data = response.json()
    anime = data['anime']
    character = data['character']
    quote = data['quote']

    tweet ="Anime quote #" + str(a) + "\n\n'" + quote + "'" + '\n\n-' + character + ',\n ' + anime + '\n#Anime'
    
    return tweet 

a = 14

for i in range(1):
        
    a += 1
    hello = getQuote()
    
    api.update_status(hello)
    print("Tweeted")
    time.sleep(30)





