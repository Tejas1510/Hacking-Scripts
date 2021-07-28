# Importing required libraries
from selenium import webdriver

# Specifying the webdriver path
driver = webdriver.Chrome("your_webdriver_path")

# Specifying the URL of the page whose table is to be scrapped

driver.get('your_website_url')

# Maximizing the web page window to test the above mentioned URL opens through the chrome driver or not
driver.maximize_window()

# Specifying the XPath of all the td(or column tags)

column_1 = driver.find_elements_by_xpath('your_xpath_column_1')
column_2 = driver.find_elements_by_xpath('your_xpath_column_2')
column_3 = driver.find_elements_by_xpath('your_xpath_column_3')
column_4 = driver.find_elements_by_xpath('your_xpath_column_4')
column_5 = driver.find_elements_by_xpath('your_xpath_column_5')
column_6 = driver.find_elements_by_xpath('your_xpath_column_6')

# Creating loop to get all records

result = []
for i in range(len(column_1)):
    temporary_data={'column_1': column_1[i].text,
                   'column_2': column_2[i].text,
                   'column_3': column_3[i].text,
                   'column_4': column_4[i].text,
                   'column_5': column_5[i].text,
                   'column_6': column_6[i].text}
    result.append(temporary_data)

# Coverting raw data into DataFrame

import pandas as pd
df_data = pd.DataFrame(result)
print(df_data)

# Converting DataFrame to .CSV and excel file

# For Excel
df_data.to_excel('result.xlsx', index =False)

# For Csv
df_data.to_csv('result.csv', index =False)

