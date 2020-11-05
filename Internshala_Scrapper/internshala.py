# This script will scrape all the internships with given url
# and create a CSV sheet out of it.

# Necessary imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# A dictionary that will initially hold all scraped values
scraped_data = {
    'heading': [],
    'company': [],
    'stipend': [],
    'apply_by': [],
    'start_date':[],

}

main_url=input("Please enter the url of internshala website to scrap : ")

url = main_url
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
count_of_internships = int(soup.find("div",
                                     class_="heading_4_6").text.split()[0])

num_of_pages = int((count_of_internships / 40) + 1)
# A loop that will go to each page and will scrape the data
for i in range(1, num_of_pages + 1):
    # ------------------- Scraping starts here -------------------------------
    response = requests.get(f"{url}/page-{0}".format(i))
    print("Please Wait , We are scrapping the details")  # Check out response whether its 200 or not

    # ........ if response is not 200, exit the script ..........
    if response.status_code != 200:
        print("Task cannot be completed at the moment!!!")
        exit()

    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

# ------------------- Search for heading of the Internship -------------------
    heading_data = soup.find_all("div", class_="heading_4_5 profile")
    for heading in heading_data:
        scraped_data['heading'].append(heading.text.lstrip('\n'))

# ------------------- Search for company of the Internship -------------------
    company_data = soup.find_all("div", class_="company_name")
    for name in company_data:
        # Cleaning of data before saving it
        name = name.text
        name = name.lstrip('\n')
        name = name.lstrip(' ')
        name = name.rstrip('\n')
        name = name.rstrip(' ')
        scraped_data['company'].append(name)


# ------------------- Search for stipend of the Internship -------------------
    stipend_data = soup.find_all("span", class_="stipend")
    for stipend in stipend_data:
        stipend = stipend.text
        stipend = stipend.lstrip('\n')
        stipend = stipend.lstrip(' ')
        stipend = stipend.rstrip('\n')
        stipend = stipend.rstrip(' ')
        scraped_data['stipend'].append(stipend)

# ------------------- Search for apply by date of the Internship -------------
    apply_by_data = soup.find_all("div", class_="apply_by")
    for apply_date in apply_by_data:
        apply_date = apply_date.find("div", class_="item_body").text
        apply_date = apply_date.lstrip('\n')
        apply_date = apply_date.lstrip(' ')
        apply_date = apply_date.rstrip('\n')
        apply_date = apply_date.rstrip(' ')
        scraped_data['apply_by'].append(apply_date)

    duration_data = soup.find_all("div", class_="internship_other_details_container")
    for duration in duration_data:
        # Cleaning of data before saving it
        duration = duration.find("div", class_="item_body").text
        duration = duration.lstrip('\n')
        duration = duration.lstrip(' ')
        duration = duration.rstrip('\n')
        duration = duration.rstrip(' ')
        scraped_data['start_date'].append(duration)

# ------------------- Search for logo of the company of the Internship -------

# Now convert the obtained dictionary to a CSV file via pandas module
df = pd.DataFrame(scraped_data)
df.to_csv('internships1.csv', index=False)
