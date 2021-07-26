# Importing required libraries
from selenium import webdriver

# Specifying the webdriver path
driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

# Specifying the URL of the page whose table is to be scrapped

driver.get('https://www.nirfindia.org/2020/UniversityRanking.html')

# Maximizing the web page window to test the above mentioned URL opens through the chrome driver or not
driver.maximize_window()

# Specifying the XPath of all the td(or column tags)

institute_id = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[1]')
name = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[2]')
city = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[3]')
state = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[4]')
score = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[5]')
rank = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[6]')

# Creating loop to get all records

nirf_result = []
for i in range(len(city)):
    temporary_data={'Institute Id': institute_id[i].text,
                   'Name': name[i].text,
                   'City': city[i].text,
                   'State': state[i].text,
                   'Score': score[i].text,
                   'Rank': rank[i].text}
    nirf_result.append(temporary_data)

# Coverting raw data into DataFrame

import pandas as pd
df_data = pd.DataFrame(nirf_result)
print(df_data)
