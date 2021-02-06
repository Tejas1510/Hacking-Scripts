
import discord
from discord.ext import commands,tasks
from bs4 import BeautifulSoup as Soup
import requests
from random import choice
import json

#You can change the command prefix to anything!

bot = commands.Bot(command_prefix='!')

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})

@bot.event
async def on_ready():
	print("Bot is running!")

with open("memes.json", "r") as f:
    src = json.load(f)

gif = []

@bot.command()
#change the role or remove this command
# @commands.has_role("your role here!")
async def scrapeurl(ctx,url):
    htm = s.get(url)
    soup = Soup(htm.text, "html.parser")
    for img in soup.findAll('img',attrs={'class':'resp-media'}):
        if "data:image/" in str(img):
            gif.append(img['src'])
        else:
            src.append(img['src'])
    with open("memes.json","w") as f:
        json.dump(src,f)

@bot.command()
async def meme(ctx):
    #put The channel Id you want to message in
    channel = bot.get_channel(Your channel ID)
    # Example:
    #channel = bot.get_channel(807568989695721504)
    await channel.send(choice(src))


bot.run('YOUR BOT TOKEN')
