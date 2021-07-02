# Tiffin-Booking-System
This is a non-GUI Python-MySQL integrated system which is based on the topic "Tiffin Booking System".While booking(ordering) thing on the internet you may be curious to know about how these system work in the background , tiffin-booking system can make you understand the same and the programmers can get to know about the login-system logic as well as a better understanding about the conditional (if-else) statements .
The various options available for the users include :-

* Sign-Up
* Log-In
* Book the Tiffin
* Check the booked Tiffin Status
* Check Tiffin and Customer Details
* Update Details
* Cancel Tiffin Subscription
* Master Login (by this the owner of the tiffin company can check the total sale the no.of accounts created )

The data that will be entered by the user will be saved , updated in the sql database that will be locally created and stored.

Kindly read the instructions given below throughly to setup the project successfully on your local machine.

# Tech Stack
* Python
* MySQL

# Prerequsites
* Python
    * IDE
* Python Libraries
    * pandas
    * getpass
    * os
    * tabulate
    * datetime
    * mysql.connector
* MySQL
   * Server
   * Workbench     
# Installation
* Python : [https://www.python.org/downloads](https://www.python.org/downloads)
* Libraries : Use the pip install library_name command in terminal to install all libraries
* MySQL : [https://dev.mysql.com/downloads](https://dev.mysql.com/downloads)
# Setting Up 
* Download both the python(.py) and mysql(.sql) file.
* Open the MySQL Workbench and open the mysql(.sql) script file which you have downloaded.
* Now follow the instructions strictly in the commented section and run the statements one by one from top to bottom.
    * WARNING! Don't make any changes in the table name and delete the database with the similar name as the script if you have any.
    * WARNING! Run the statement to create customer_info table at the end after creating all other tables from Tiffin_Type to Master_Login as it contains foreign key constraints.
* When you reach at the point creating Master_Login table ,create the table and before inserting values in it you can change the master username and password by changing the create_username and create_password under the quoted marks according to yourself.
![IMAGE:](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/master_table_instruction.png)
* After running all the statements use the SHOW TABLES; statement and verify that you have created all the tables successfully.
* Now open the python(.py) file while you have earlier downloaded and run the code.
     * WARNING! Visual Studio Code is recommended as some libraries may not work in terminal or other python IDE's.
* Now in the 11th line use your mysql user and password in place of your_user and your_mysql_password respectively if you have not set the password then remove the passwd word.

If you have set the password
![IMAGE:](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/sql_connector_1.png)
If you have not set the password
![IMAGE:](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/sql_connector_2.png)

* You have successfully started the Tiffin-Booking System ,you can now follow the instruction and explore it.
# How To Use
* Here are some snips showing an example user using the system

* User is asked for Sign-Up or login choice ![1](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/1.png)
* User enters the detail and the account is successfully created ![2](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/2.png)
* User is now asked to Log-In from the created username,password and is then asked to select from the choices ![3](https://github.com/Rajulmahto21/Hacking-Scripts/blob/main/Python/Tiffin%20Booking%20System/How%20To%20Use%20Snips/3.png)
* User selects Book Your Tiffin and then tiffin menu is shown ![4](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/4.PNG)
* User is asked to enter the tiffin and days choices ![5](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/5.PNG)
* User enters the day choice and enter's y to get the order summary and the order summary is displayed  ![6](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/6.PNG)
* User is asked to enter yes to confirm his tiffin order then the order is confirmed and he receives the unique booking ID ![7](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/7.PNG)
* This time user logs in and selects Check Tiffin Status and then enters the booking ID,the tiffin status is displayed ![8](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/8.PNG)
* User selects Check Tiffin and Customer Details ,the order and customer details are shown ![9](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/9.PNG)
* User selects Update details  ![10](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/10.PNG)
* User selects to change name and the name gets updated ![11](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/11.PNG)
* User selects to change address and the address gets updated ![12](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/12.PNG)
* User selects to change contact and the contact gets updated ![13](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/13.PNG)
* User selects to change email address and the email address gets updated ![14](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/14.PNG)
* User views the updated details,the details are updated ![15](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/15.PNG)
* This time user selects to cancel tiffin choice ,users is asked to type yes to cancel,the tiffin service gets cancelled ![16](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/16.PNG)
* User selects to master login to view company statistics ,total sale,account & customer count with average tiffin cost is shown ![17](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/17.PNG)
* ER Diagram Of The DataBase ![sql](https://github.com/Rajulmahto21/Tiffin-Booking-System/blob/main/How%20To%20Use%20Snips/ER_DIAGRAM.png)
      
        

      
       
