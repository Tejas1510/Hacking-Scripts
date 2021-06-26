import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.goodreturns.in/gold-rates/")
Soup = BeautifulSoup(page.content,'html.parser')

info = Soup.find_all(class_="odd_row")
count = 0

for items in info:
    count +=1
    if count ==2:
        print(items.get_text())
        break