import requests
import bs4
print("England tour of Sri Lanka, 2021")

link = 'https://www.cricbuzz.com/live-cricket-scorecard/32248/sl-vs-eng-2nd-test-england-tour-of-sri-lanka-2021'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text,'html.parser')

details = soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
for i in details:
 print(i.getText().strip())
#.cb-col .cb-col-100 .cb-scrd-hdr-rw
#https://www.cricbuzz.com/live-cricket-scorecard/32303/ban-vs-wi-2nd-odi-west-indies-tour-of-bangladesh-2021'
