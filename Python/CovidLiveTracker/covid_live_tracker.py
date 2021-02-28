from bs4 import BeautifulSoup
import requests
import csv
import re

print('Collecting data ...')
# Creating an object of Scrapper type and passing on the url
soup = BeautifulSoup(requests.get(
    "https://www.worldometers.info/coronavirus/").text, 'lxml')
# Searching for tables in the page"
table = soup.find("table", {"id": "main_table_countries_today"})
# Extracting the headers of the table and performing some data cleaning
headings = [h.text.replace('\n', '').replace('\xa0', '')
            for h in table.find_all('th')]
# Extracting only the country wise data by deleting the continent wise data
rows = [r for r in table.find_all('tr') if not r.has_attr('data-continent')]
# Removing the header
rows = rows[1:]
# Stoeing the result
result = []
flag = 0
result.append(headings)
for table_row in rows:
    row = []
    for data in table_row.find_all('td'):
        if data.a is not None:
            row.append(data.a.text)
        else:
            row.append(data.text)
    result.append(row)
# Storing the data in a csv
csv_file = open('data.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerows(result)
csv_file.close()

# Getting the input Country name from the user for which he wants the COVID live stats
country = input('Enter country name --- ')

# Opening the database ,searching for the record ,then retrieving the values accordingly
with open('data.csv') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if(re.match(country, row[1], re.IGNORECASE)):
            flag = 1
            print('Country - ', row[1])
            if(len(row[2]) > 0):
                print('Total Cases - ', row[2])
            else:
                print('Total Cases - ', '0')
            if(len(row[4]) > 0):
                print('Total Deaths - ', row[4])
            else:
                print('Total Deaths - ', '0')
            if(len(row[6]) > 0):
                print('Total Recovered - ', row[6])
            else:
                print('Total Recovered - ', '0')
            if(len(row[3]) > 0):
                print('Newly Reported Cases - ', row[3])
            else:
                print('Newly Reported Cases - ', '0')
            if(len(row[5]) > 0):
                print('Newly Reported deaths - ', row[5])
            else:
                print('Newly Reported Deaths  - ', '0')
            if(len(row[7]) > 0):
                print(' Newly Recovered - ', row[7])
            else:
                print('Newly Recovered  - ', '0')

# Flag for checking , in case a wrong country name is given
if(flag == 0):
    print("No such country exists")
