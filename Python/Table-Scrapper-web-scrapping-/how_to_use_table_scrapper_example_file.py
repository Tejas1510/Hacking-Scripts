from selenium import webdriver

driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

driver.get('https://www.nirfindia.org/2020/UniversityRanking.html')
driver.maximize_window()

institute_id = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[1]')
name = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[2]')
city = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[3]')
state = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[4]')
score = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[5]')
rank = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[6]')

nirf_result = []
for i in range(len(city)):
    temporary_data={'Institute Id': institute_id[i].text,
                   'Name': name[i].text,
                   'City': city[i].text,
                   'State': state[i].text,
                   'Score': score[i].text,
                   'Rank': rank[i].text}
    nirf_result.append(temporary_data)

import pandas as pd
df_data = pd.DataFrame(nirf_result)
print(df_data)
df_data.to_excel('nirf_ranking_result.xlsx', index =False)
df_data.to_csv('nirf_ranking_result.csv', index =False)
