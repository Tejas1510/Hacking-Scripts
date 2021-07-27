# Table-Scrapper-web-scrapping-
This is a python script which will help you to scrap out table from any HTML based websites on the internet,sometimes while creating a script ,project or system we need some data from a website or a web page which may be in the form of tables,some script require a .CSV or an excel file is required in order for them to work.
So this python script will help users to scrap tables from the web pages and automatically convert them to .CSV or an excel file so that it can be used in the projects or databases.This will include the following :

* Entering the URL
* Entering the required information to scrap out tables
* Converting them to DataFrame
* Finally converting them to .CSV or an excel file.

<b>Advantages of this script</b>

* It will be really efficient to scrap out tables in just seconds.
* It will save a lot of time.
* Users can also get the updated tables which they could not get if they copy or manually enter data.
* Programmers can get to know more about "WEB SCRAPPING" from this script.

# Tech Stack
* Python

# Prequsites
* Python
   * IDE (Jupyter Notebook is the recommended IDE )
* Python Libraries
   * Selenium
   * Pandas
* Web Driver (of your browser you are going to use recommended is google chrome)

# Installation
* Python : [https://www.python.org/downloads](https://www.python.org/downloads)
* IDE : [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) (followed by installation of jupyter notebook)
* Libraries: Open the directory of your installed python version in command prompt and type the following lines followed by pressing enter
    * For Selenium: `pip install selenium`
    * For Pandas: `pip install pandas`
* Web Driver : [https://www.selenium.dev/downloads](https://www.selenium.dev/downloads)
   * Open the above link and scroll down to "Browser" now click on the documentation link of your browser, here i will show for google chrome.![1](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/1.PNG)
   * Now download the  ChromeDriver 91.0.4472.101 (recommended).![2](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/2.PNG)
   * Now extract the zip and remember the path of extracted chrome driver.

# Setting Up
* Download the Table Scrapper.py file from above and open it in jupyter notebook.
* Now write the path where you extracted the google chrome web driver in place of "your_webdriver_path".
    * `driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")`
* Now write the URL of the website in which the table to be scrapped is present in place of "your_website_url"
   * `driver.get('https://www.nirfindia.org/2020/UniversityRanking.html')`
* Now write the XPath of the columns in place of "your_xpath_column_1" which you want to have in your csv or an excel file table and write all the XPath of column if you dont know to write the XPath you can refer to the example i have shown in how to use section.
   * `column_1 = driver.find_elements_by_xpath('//table[@id="tbl_overall"]/tbody/tr/td[1]')`

# How To Use
<b>Here i will show you how to use the script and here i have used a table in the below link which is to be scrapped</b>
[https://www.nirfindia.org/2020/UniversityRanking.html](https://www.nirfindia.org/2020/UniversityRanking.html)

* This is the table to be scrapped and we will copy this link and paste it in the script. `driver.get('https://www.nirfindia.org/2020/UniversityRanking.html')`
![3](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/3.PNG)
* Now right click on the page and select inspect from the drop down.![4](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/4.PNG)
* So first of all we have to get the table id which we want ,for this look for the table HTML tag so that we can find the table id easily now as you will hover the cursor over the table id you can see the table being hightlighted in the webpage as you can see in the screenshot so in my case the table id is 
`table id="tbl_overall"`![5](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/5.png)
* Now to get the desired columns for our table we have to get their XPath ,which will be then used in a loop to get all the rows in the.
  So to get XPath turn on the select element to inspect option at the top left corner as shown in the image below then, hover over the first row element on that column selected whose XPath we need then in the inspection window you will see the respective code highlighted ,now right click on the code,now click on copy, then copy XPath.
In the example below to get all the institute id we will hover over the first record of the instute id named IR-O-U-0220 and then right click on the highlighted code to copy XPath as shown.
![6](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/6.png)
![7](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/7.png)

* Now in the python script paste the XPath in place of the brackets and write the corresponding name of the column in varibale, do same for all columns and copy their respective XPaths to their column name ,you can also add more columns.![8](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/8.png)
* Now in the next part of the code `for i in range(len(city)):` in place of city you can specify any column name to get the length of the full table (i.e, all the records).
* Now you have to keep the variable name same as you typed in starting in the next part of the code as shown below
![9](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/9.png)
* Now in the next part we will create a dataframe of all the collected data using the pandas library and ultimately converting it into csv or an excel file which will be saved locally.
![10](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/10.png)
* The whole code will look someting like this.
![11](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/11.png)
* Now run the cells in order as shown in the below clip to finally generate a csv or an excel file.
![table scrapping](https://user-images.githubusercontent.com/59139755/127117991-15c7ee85-e3bf-4c01-aa7b-07abdfdcfac3.gif)

* You can use
   * `df_data.to_excel('nirf_ranking_result.xlsx', index =False)` for excel file.
   * `df_data.to_csv('nirf_ranking_result.csv', index =False)` for .csv file.

* The excel file generated 

![12](https://github.com/Rajulmahto21/Table-Scrapper-web-scrapping-/blob/main/Snips/12.PNG)





