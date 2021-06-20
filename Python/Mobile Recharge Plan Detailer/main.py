import requests
from bs4 import BeautifulSoup

user= (input("enter your service provider : "))
url ="https://www.91mobiles.com/recharge-plans/"+user+"-prepaid-gujarat-unlimited"

page =requests.get(url)
Soup =BeautifulSoup(page.content,'html.parser')

info =Soup.find_all(class_='ofr-desc')
a= [items.get_text() for items in info]

for i in a:
  print(i)
