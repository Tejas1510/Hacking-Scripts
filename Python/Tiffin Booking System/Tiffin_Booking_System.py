# Including all the libraries
import pandas as pd 
import getpass
import os
from tabulate import tabulate
from datetime import date
import mysql.connector

# Connecting with the mysql database

mydb= mysql.connector.connect(host="localhost", user="your_user", passwd="your_mysql_password", database="project", auth_plugin="mysql_native_password")
cursor = mydb.cursor()

# For the title to be in centre

width=os.get_terminal_size().columns
print("WELCOME TO THE TIFFIN BOOKING SYSTEM".center(width))

# Login or SignUp Choice
print("")
SignUp_Choice=input("Do you want to create a new account type YES to create a new account or type no to login :")
print("")

if SignUp_Choice=="no": # If choice is no the options to book,etc will be available after entering the username and password
    Enter_username=input("Enter UserName:")
    Enter_Password= getpass.getpass("Enter Password:") # Getpass library used to hide the password typed by the user
    cursor.execute("""SELECT Create_Password FROM customer_info 
                             WHERE Username= %s""", (Enter_username , ) ) # Checking if the login information entered exists in the database
    result=cursor.fetchone()
    if result==None: #If the entered password or username is wrong or the username doesnot exists the error message is displayed
        print("Username or  Password  entered is incorrect")
        exit()
    for row in result:
        Data=row
        
    cursor.execute("""SELECT Username FROM customer_info
                             WHERE Create_Password= %s""", (Enter_Password , ) )
    
    result1=cursor.fetchone()
    if result1==None:
        print("Username or  Password  entered is incorrect")
        exit()
    for row1 in result:
        Data1=row1
        
        if Data==Enter_Password: # If the information is enetred is correct the options are shown
            print("LogIn Successful")
            print("")
            print("Press the corresponding number to navigate")
            print("""   
                        1 == Book your Tifffin
                        2 == Check Tiffin Status
                        3 == Check Tiffin and Customer Details
                        4 == Update Details
                        5 == Cancle Tiffin Subscription
                        6 == Master Login
                        """
                )

            # The menu is displayed and the user enters their choice and the accordingly the information is displayed

            option_selection=int(input("Enter your choice:"))

            # This option is used to book the tiffin

            if option_selection==1:
                print("")
                print("RESTAURANT'S MENU:")
                print("")
                a1=['Alu+Roti(6 pic)+Dahi+Chatni+DalPalak+Rice+Salad','DamAlu+MethiParatha+DalRice+Salad','MutterPanner+Roti(6 piece)Dal+Pulao+Salad','Chole+Puri+Dal+Rice+Salad+GreenVagitables+FruitSalad','Paneer+Roti+Sambar+Roti+Salad','MixVeg Dal+PlaneRice+Salad+Roti(6 piece)+Shira','Rajma+Dal+Roti(6 piece)+Rice+Onion']                    
                table1={'DAYS':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
                        'BREAKFAST (7:00 AM -10:00 AM)':['Puri+Aloo chana Sabji','Plane Paratha + Aloo Sabji',' Poha','Upma','Puri + Aloo Sbji','Paratha + Chatni ','Chowmine'],
                        'LUNCH (12:00-2:00 PM)':['Rice+Dal+Sabji+Salad+Roti ','Rice+AlooGovi Sabji +Dal+Salad','Rice+Egg+Curry+Dal+Roti(7+Salad)','Rice + Rajma+Dal','Rice+Green Vagitables+Roti+Chips','FriedRice+Dal+Chatni+Roti','Rice+Dal+Roti+Salad'],
                        'Dinner(7:00 PM-12:00 AM)':a1}
                t=tabulate(table1,tablefmt="pretty",headers=['DAYS','BREAKFAST (7:00 AM -10:00 AM)','LUNCH (12:00-2:00 PM)','Dinner(7:00 PM-12:00 AM)'])
                print(t)
                print("")
                info= {"Tiffin":["Breakfast(7:00 AM -10:00 AM)","Lunch(12:00-2:00 PM)","Dinner(7:00 PM-12:00 AM)"],"Cost":[120,180,300]}
                ind={1,2,3}
                df = pd.DataFrame(info,index=ind)
                print(df)
                print("")
                print("Press the corresponding numbers to select items:")
                print("")
                print("Press the correspinding number and press enter each time to add items")
                print("If you are done adding items then enter 8 as the item choice and press enter,your above choices will be recorded")
                print("WARNING! Your Previously entered choices for tiffin will be deleted please enter all your choices again as per above MENU ")
                print("")
                
                # The choices entered by the user is store in the table with their corresponding usernames

                Tiffin_Choice=0
                cursor.execute("""DELETE FROM User_TiffinChoice WHERE Username= %s""",(Enter_username , ))
                while Tiffin_Choice!=8:
                    Tiffin_Choice=int(input("Enter Item Number:"))
                    if Tiffin_Choice==1:
                        sql_syntax = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                        values =(Enter_username,Tiffin_Choice)
                        cursor.execute(sql_syntax, values)
                        mydb.commit()

                    if Tiffin_Choice==2:
                        sql_syntax1 = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                        values1 =(Enter_username,Tiffin_Choice)
                        cursor.execute(sql_syntax1, values1)
                        mydb.commit()
              
                    if Tiffin_Choice==3:
                        sql_syntax2 = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                        values2 =(Enter_username,Tiffin_Choice)
                        cursor.execute(sql_syntax2, values2)
                        mydb.commit()
                
                    if Tiffin_Choice==8:
                        break
                
                # The total cost is calculated according to the choices entered by the users are is stored in the database

                cursor.execute("""SELECT SUM(b.Cost) FROM User_TiffinChoice a JOIN Tiffin_Type b ON a.Tiffin_Choice_Id=b.Tiffin_Id WHERE a.Username= %s""",(Enter_username , ))
                Total_Cost=cursor.fetchone()
                for cost in Total_Cost:
                    print("")
                    print("Your Total Cost is:",cost,"Rupees")
                    print("")

                # User is made to enter the days on which they require tiffin

                print("Enter the corresponding day number to select days on which tiffin is to be delivered")
                print("")
                print("""
                        1 == Monday
                        2 == Tuesday
                        3 == Wednesday
                        4 == Thrusday
                        5 == Friday
                        6 == Saturday
                        7 == Sunday
                        """
                    )

                # The day choices are also stored in the database with their respective usernames

                Day_Choice=0
                cursor.execute("""DELETE FROM User_TiffinDays WHERE Username= %s""",(Enter_username , ))
                while Day_Choice!=8:
                    Day_Choice=int(input("Enter Day Number:"))
                    if Day_Choice==1:
                        sql_syntax_day1 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day1 =(Enter_username,"Monday")
                        cursor.execute(sql_syntax_day1, values_day1)
                        mydb.commit()

                    if Day_Choice==2:
                        sql_syntax_day2 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day2 =(Enter_username,"Tuesday")
                        cursor.execute(sql_syntax_day2, values_day2)
                        mydb.commit() 

                    if Day_Choice==3:
                        sql_syntax_day3 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day3 =(Enter_username,"Wednesday")
                        cursor.execute(sql_syntax_day3, values_day3)
                        mydb.commit() 

                    if Day_Choice==4:
                        sql_syntax_day4 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day4 =(Enter_username,"Thursday")
                        cursor.execute(sql_syntax_day4, values_day4)
                        mydb.commit() 

                    if Day_Choice==5:
                        sql_syntax_day5 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day5 =(Enter_username,"Friday")
                        cursor.execute(sql_syntax_day5, values_day5)
                        mydb.commit() 

                    if Day_Choice==6:
                        sql_syntax_day6 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day6 =(Enter_username,"Saturday")
                        cursor.execute(sql_syntax_day6, values_day6)
                        mydb.commit()

                    if Day_Choice==7:
                        sql_syntax_day7 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                        values_day7 =(Enter_username,"Sunday")
                        cursor.execute(sql_syntax_day7, values_day7)
                        mydb.commit()                                   
                
                    if Day_Choice==8:
                        break

                # After enterinng the day choices the data stored until now is fetched fromt the database and shown to the user
                    
                Order_Summary=0
                while Order_Summary!="y":
                    Order_Summary=input("Please press y to get your order sumary:")
                    if Order_Summary=="y":
                        print("")
                        print("ORDER SUMMARY:")
                        print("")
                        cursor.execute("""SELECT Name FROM customer_info
                                 WHERE Username= %s""", (Enter_username , ))
                        result_name=cursor.fetchone()
                        for name in result_name:
                            print("Name:",name)
                        cursor.execute("""SELECT Address FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                        result_address=cursor.fetchone()
                        for address in result_address:
                            print("Address:",address)
                        cursor.execute("""SELECT Contact FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                        result_contact=cursor.fetchone()
                        for contact in result_contact:
                            print("Contact Number:",contact)
                        cursor.execute("""SELECT Email FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                        result_email=cursor.fetchone()
                        for email in result_email:
                            print("Email Address:",email)
                        cursor.execute("""SELECT Tiffin_Type.Tiffin_Id,Tiffin_Type.Tiffin,Tiffin_Type.Cost
                              FROM Tiffin_Type
                              INNER JOIN User_TiffinChoice ON
                              Tiffin_Type.Tiffin_Id=User_TiffinChoice.Tiffin_Choice_Id
                              WHERE User_TiffinChoice.Username  = %s""", (Enter_username , ))
                        result_selected_orders=cursor.fetchall()
                        for orders in result_selected_orders:
                            print("Selected Orders are:",*orders)
                        cursor.execute("SELECT Tfiini_Days_Choice FROM User_TiffinDays WHERE Username=%s", (Enter_username , ))
                        result_selected_orders_days=cursor.fetchall()
                        for days in result_selected_orders_days:
                            print("Selected Days are:",*days)  


                # After the users types yes the user id with the selected order,days,total cost,etc are stored in a seperate table in the database so as to maintain the records of the confirmed orders
                # At this stage the users are assigned a special ID through which they can track their status and get their order details , at this stage the delivery boy is also assigned will will be reflected in the order details
                print("")
                OrderConfirmation_Choice=input("Type yes if you want to confirm your orders or press no to exit:")
                if OrderConfirmation_Choice=="yes":
                    cursor.execute("""SELECT User_Id FROM customer_info WHERE Username = %s""", (Enter_username , ))
                    result_ID=cursor.fetchone()
                    for ID in result_ID:
                        Customer_ID=ID
                    today = date.today()    
                    formatted_date = today.strftime('%Y-%m-%d')    
                    sql_syntax3= "INSERT INTO Delivery_info (Customer_ID ,TiffinBoy_Name,TiffinBoy_Phone_Number,Delivery_Address ,Customer_Contact,Customer_Name,Order_Status,Order_Days,DeliverOrder_Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values3 =(Customer_ID,'Arun Singh',9893498910,address,contact,name,'Booked','User Chosen Days',formatted_date)
                    cursor.execute(sql_syntax3,values3)
                    mydb.commit()
                    
                    sql_syntax_sum= "INSERT INTO User_TotalCost (User_cost,Username) VALUES(%s,%s)"
                    values_sum=(cost,Enter_username)
                    cursor.execute(sql_syntax_sum,values_sum)
                    mydb.commit()
                    
                    cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Customer_ID = %s""", (ID , ))
                    result_orderid=cursor.fetchone()
                    for print_orderid in result_orderid:
                        show_orderid=print_orderid
                    print("")
                    print("Ordered Successfully!!")
                    print("")
                    print("Your Order ID is:",show_orderid)
                    exit()
                
                if OrderConfirmation_Choice=="no":
                    
                    exit()
            
            # This option is used to check the tiffin status with the help of your unique ID

            if option_selection==2:
                order_id_input=int(input("Enter Your Order ID:"))
                cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Order_ID = %s  """ , (order_id_input , ))
                result_order_id_output=cursor.fetchone()
                if result_order_id_output==None:
                    print("OrderID entered is incorrect Please restart the program")
                    exit()
                for orderid_forchecking in result_order_id_output:
                    orderid_data=orderid_forchecking
                if order_id_input==orderid_data:
                    cursor.execute("""SELECT Order_Status FROM Delivery_info
                              WHERE Order_ID= %s""", (order_id_input , ))
                    result_Order_Status=cursor.fetchone()
                    for Order_Status in result_Order_Status:
                        print("Tiffin Status:",Order_Status)
                    cursor.execute("""SELECT DeliverOrder_Date FROM Delivery_info
                              WHERE Order_ID= %s""", (order_id_input , ))
                    result_DeliverOrder_Date=cursor.fetchone()
                    for DeliverOrder_Date in result_DeliverOrder_Date:
                        print("Tiffin Booking Date:",DeliverOrder_Date)
                        exit()
            
            # This option is used to check the tiffin and customer details with the help of the unique ID

            if option_selection==3:
                order_id_input1=int(input("Enter Your Order ID:"))
                cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Order_ID = %s  """ , (order_id_input1 , ))
                result_order_id_output1=cursor.fetchone()
                if result_order_id_output1==None:
                    print("OrderID entered is incorrect or you have not booked any tiffin Please restart the program")
                    exit()
                for orderid_forchecking1 in result_order_id_output1:
                    orderid_data1=orderid_forchecking1
                if order_id_input1==orderid_data1:
                    print("TIFFIN & BILLING DETAILS:")
                    print(" ")
                    cursor.execute("""SELECT Name FROM customer_info
                                 WHERE Username= %s""", (Enter_username , ))
                    result_name1=cursor.fetchone()
                    for name1 in result_name1:
                        print("Name:",name1)
                    cursor.execute("""SELECT Address FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                    result_address1=cursor.fetchone()
                    for address1 in result_address1:
                        print("Address:",address1)
                    cursor.execute("""SELECT Contact FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                    result_contact1=cursor.fetchone()
                    for contact1 in result_contact1:
                        print("Contact Number:",contact1)
                    cursor.execute("""SELECT Email FROM customer_info
                              WHERE Username= %s""", (Enter_username , ))
                    result_email1=cursor.fetchone()
                    for email1 in result_email1:
                        print("Email Address:",email1)
                    cursor.execute("""SELECT Tiffin_Type.Tiffin_Id,Tiffin_Type.Tiffin,Tiffin_Type.Cost
                              FROM Tiffin_Type
                              INNER JOIN User_TiffinChoice ON
                              Tiffin_Type.Tiffin_Id=User_TiffinChoice.Tiffin_Choice_Id
                              WHERE User_TiffinChoice.Username  = %s""", (Enter_username , ))
                    result_selected_orders1=cursor.fetchall()
                    for orders1 in result_selected_orders1:
                        print("Selected Orders are:",*orders1)
                    cursor.execute("SELECT Tfiini_Days_Choice FROM User_TiffinDays WHERE Username=%s", (Enter_username , ))
                    result_selected_orders_days=cursor.fetchall()
                    for days in result_selected_orders_days:
                        print("Selected Days are:",*days)
                        
                    cursor.execute("""SELECT User_cost FROM User_TotalCost WHERE Username=%s""", (Enter_username , ))
                    result_cost_user=cursor.fetchone()
                    for TOTAL_COST in result_cost_user:
                        print("Your Total Cost is:",TOTAL_COST,"Rupees")
                        
                    print("Tfffin Delivery Details:")
                    print(" ")
                    cursor.execute("""SELECT TiffinBoy_Name FROM Delivery_info
                                 WHERE Order_ID= %s""", (order_id_input1 , ))
                    result_tiffinboyname=cursor.fetchone()
                    for tiffinboyname in result_tiffinboyname:
                          print("Tiffin Boy Name:",tiffinboyname)
                          
                    cursor.execute("""SELECT TiffinBoy_Phone_Number FROM Delivery_info
                                 WHERE Order_ID= %s""", (order_id_input1 , ))
                    result_tiffinboyphone=cursor.fetchone()
                    for tiffinboyphone in result_tiffinboyphone:
                        print("Tiffin Boy Phone No:",tiffinboyphone)
                exit()

            # This option is used by the owner of the tiffin service (in this case we can all login) this includes a special login and passwords which can be easily set in the database scsripts

            if option_selection==6:
                Enter_master_username=input("Enter Master UserName:")
                Enter_master_Password= getpass.getpass("Enter Master Password:")
                cursor.execute("""SELECT Master_Password FROM Master_Login
                         WHERE Master_Username= %s""", (Enter_master_username , ) )
                result_master=cursor.fetchone()
                if result_master==None:
                    print("Master Username entered is incorrect")
                    exit()
                for row_master in result_master:
                    Data_master=row_master

                cursor.execute("""SELECT Master_Username FROM Master_Login
                        WHERE Master_Password= %s""", (Enter_master_Password , ) )
                result1_master=cursor.fetchone()
                if result1_master==None:
                    print("Master Password entered is incorrect")
                    exit()
                for row1_master in result_master:
                    Data1_master=row1_master
                    if Data_master==Enter_master_Password:
                        print("LogIn Successful")
                        print("COMPANY STATISTICS ARE:")
                        cursor.execute("SELECT SUM(b.Cost) FROM User_TiffinChoice a JOIN Tiffin_Type b ON a.Tiffin_Choice_Id=b.Tiffin_Id")
                        result_totalsale=cursor.fetchone()
                        for resulttotalsale in result_totalsale:
                            print("Total Sale:",resulttotalsale)
                        cursor.execute("SELECT COUNT(User_ID) AS NumberofAccounts FROM customer_info")
                        result_totalaccount=cursor.fetchone()
                        for resulttotalaccount in result_totalaccount:
                            print("Account Count:",resulttotalaccount)
                        cursor.execute("SELECT COUNT(Order_ID) AS NumberofCustomers FROM Delivery_info")
                        result_totalcustomers=cursor.fetchone()
                        for resulttotalcustomers in result_totalcustomers:
                            print("Customer Count:",resulttotalcustomers)
                        average=resulttotalsale/resulttotalcustomers
                        print("Averge Tiffin Order Cost:",average)

            # This option is used to Cancle Tiffin Subscription,deletes the stored data of the choices of order,days 

            if option_selection==5:
                delete_tiffinsubscription=input("Do You reall want to unsubscribe to the tiffin service with Username " + str(Enter_username) + " (yes/no):")
                if delete_tiffinsubscription=="yes":
                    cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                    result_for_userid=cursor.fetchone()
                    for finalresult_userid in result_for_userid:
                        finalresult1_userid=finalresult_userid
                        delete_statement= """DELETE FROM User_TiffinChoice WHERE Username=%s"""
                        cursor.execute(delete_statement, (Enter_username,))
                        mydb.commit()
                        delete_statement1= """DELETE FROM Delivery_info WHERE Customer_ID=%s"""
                        cursor.execute(delete_statement1, (finalresult1_userid,))
                        mydb.commit()
                        delete_statement2= """DELETE FROM User_TiffinDays WHERE Username=%s"""
                        cursor.execute(delete_statement2, (Enter_username,))
                        mydb.commit()
                        print("Tfffin service unsubscribed")
                        exit()
                    exit()
                if delete_tiffinsubscription=="no": 
                    exit()

            # This option is used to Update the customer details name ,address ,contact ,email and the same also gets updated in the database

            if option_selection==4:
                print(" What Do You Want To Update ? Press the corresponding number to navigate WARNING! You can update only one detail at a time please restart the programm to update multiple details")
                print("""
                        1 == Name
                        2 == Address
                        3 == Contact
                        4 == Email Address
                        """
                    )
                update_user_choice=int(input("Enter the Number:"))
                if update_user_choice==1:
                    new_name=input("Enter New Name:")
                    newname_statement= """UPDATE customer_info SET Name=%s WHERE Username =%s"""
                    values_name=(new_name,Enter_username)
                    cursor.execute(newname_statement, values_name)
                    cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                    result_for_userid1=cursor.fetchone()
                    for finalresult_userid1 in result_for_userid1:
                        finalresult1_userid1=finalresult_userid1
                    newname_statement1= """UPDATE Delivery_info SET Customer_Name=%s WHERE Customer_ID =%s"""
                    values_name1=(new_name,finalresult1_userid1)
                    cursor.execute(newname_statement1, values_name1)
                    mydb.commit()
                    print("Name Updated Successfully")
                    
                if update_user_choice==2:
                    new_address=input("Enter New Address:")
                    newaddress_statement= """UPDATE customer_info SET Address=%s WHERE Username =%s"""
                    values_address=(new_address,Enter_username)
                    cursor.execute(newaddress_statement, values_address)
                    cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                    result_for_userid2=cursor.fetchone()
                    for finalresult_userid2 in result_for_userid2:
                        finalresult1_userid2=finalresult_userid2
                    newaddress_statement1= """UPDATE Delivery_info SET Delivery_Address=%s WHERE Customer_ID =%s"""
                    values_address1=(new_address,finalresult_userid2)
                    cursor.execute(newaddress_statement1, values_address1)
                    mydb.commit()
                    print("Address Updated Successfully")
                    
                if update_user_choice==3:
                    new_contact=int(input("Enter New Contact:"))
                    newcontact_statement= """UPDATE customer_info SET Contact=%s WHERE Username =%s"""
                    values_contact=(new_contact,Enter_username)
                    cursor.execute(newcontact_statement, values_contact)
                    cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                    result_for_userid3=cursor.fetchone()
                    for finalresult_userid3 in result_for_userid3:
                        finalresult1_userid3=finalresult_userid3
                    newcontact_statement1= """UPDATE Delivery_info SET Customer_Contact=%s WHERE Customer_ID =%s"""
                    values_contact1=(new_contact,finalresult_userid3)
                    cursor.execute(newcontact_statement1, values_contact1)
                    mydb.commit()
                    print("Contact Updated Successfully")

                if update_user_choice==4:
                    new_mail=input("Enter New Email Address:")
                    newmail_statement= """UPDATE customer_info SET Email=%s WHERE Username =%s"""
                    values_mail=(new_mail,Enter_username)
                    cursor.execute(newmail_statement, values_mail)
                    mydb.commit()
                    print("Email Address Updated Successfully")
            exit()
        else:
            print("Entered Data Doesnot match Please Try Again")

# From here the else statement of the very first if statement starts i.e, if the user chooses to signup

else:
    print("Please enter the following information and PRESS ENTER to proceed") # User is asked to enter the details which is stored in the database
    print("")
    Name=input("Enter Your full Name:")
    Address=input("Enter Address:")
    Contact=int(input("Enter Contact Number:"))
    Email=input("Enter Email Address:")                  
    Username=input("Create Username:")
    Create_Password=input("Create Password:")
    Confirm_Password=input("Confirm Password:")
    while Confirm_Password !=Create_Password:
        print("Entered Password Does not Match")
        Confirm_Password=input("Confirm Password:")
        if Create_Password==Confirm_Password:
            print("Account Created Successfully!!")           
sql = "INSERT INTO customer_info (Name, Address, Contact,Email,Username, Create_Password) VALUES(%s, %s, %s, %s, %s, %s)"
vals =(Name, Address, Contact, Email,Username, Create_Password)
cursor.execute(sql, vals)
mydb.commit()
print("Account Created Successfully!!") # When all the data is succefully stored in the database the user is required to login at this point
print("")
print("Please LogIn to Continue")
print("")

Enter_username=input("Enter UserName:") # Checking if the login information entered exists in the database
Enter_Password=getpass.getpass("Enter Password:")

while Enter_username!=Username:
    print("Credentials Entered Doesnot Match LogIn Again")
    Enter_username=input("Enter UserName:")
    Create_Password=getpass.getpass("Enter Password:")
while Create_Password!=Create_Password:
    print("Credentials Entered Doesnot Match LogIn Again")
    Enter_username=input("Enter UserName:")
    Enter_Password=getpass.getpass("Enter Password:")

# From here the whole process of showing options and the their use is repeated and after the successfull usage of the available options the programm is exited

if (Enter_username==Username and Enter_Password==Create_Password):
        print("Logged In Successfully")
        print("")
        print("Press the corresponding number to navigate")
        print("""   
                        1 == Book your Tifffin
                        2 == Check Tiffin Status
                        3 == Check Tiffin and Customer Details
                        4 == Update Details
                        5 == Cancle Tiffin Subscription
                        6 == Master Login
                        """
             )
        option_selection=int(input("Enter the number:"))
        if option_selection==1:
            print("")
            print("RESTAURANT'S MENU:")
            print("")
            a1=['Alu+Roti(6 pic)+Dahi+Chatni+DalPalak+Rice+Salad','DamAlu+MethiParatha+DalRice+Salad','MutterPanner+Roti(6 piece)Dal+Pulao+Salad','Chole+Puri+Dal+Rice+Salad+GreenVagitables+FruitSalad','Paneer+Roti+Sambar+Roti+Salad','MixVeg Dal+PlaneRice+Salad+Roti(6 piece)+Shira','Rajma+Dal+Roti(6 piece)+Rice+Onion']                    
            table1={'DAYS':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
                    'BREAKFAST (7:00 AM -10:00 AM)':['Puri+Aloo chana Sabji','Plane Paratha + Aloo Sabji',' Poha','Upma','Puri + Aloo Sbji','Paratha + Chatni ','Chowmine'],
                    'LUNCH (12:00-2:00 PM)':['Rice+Dal+Sabji+Salad+Roti ','Rice+AlooGovi Sabji +Dal+Salad','Rice+Egg+Curry+Dal+Roti(7+Salad)','Rice + Rajma+Dal','Rice+Green Vagitables+Roti+Chips','FriedRice+Dal+Chatni+Roti','Rice+Dal+Roti+Salad'],
                    'Dinner(7:00 PM-12:00 AM)':a1}
            t=tabulate(table1,tablefmt="pretty",headers=['DAYS','BREAKFAST (7:00 AM -10:00 AM)','LUNCH (12:00-2:00 PM)','Dinner(7:00 PM-12:00 AM)'])
            print(t)
            print("")
            info= {"Tiffin":["Breakfast(7:00 AM -10:00 AM)","Lunch(12:00-2:00 PM)","Dinner(7:00 PM-12:00 AM)"],"Cost":[120,180,300]}
            ind={1,2,3}
            df = pd.DataFrame(info,index=ind)
            print(df)
            print("")
            print("Press the corresponding numbers to select items:")
            print("")
            print("Press the correspinding number and press enter each time to add items")
            print("If you are done adding items then enter 8 as the item choice and press enter,your above choices will be recorded")
            print("WARNING! Your Previously entered choices for tiffin will be deleted please enter all your choices again as per above MENU ")
                
            Tiffin_Choice=0
            cursor.execute("""DELETE FROM User_TiffinChoice WHERE Username= %s""",(Enter_username , ))
            while Tiffin_Choice!=8:
                Tiffin_Choice=int(input("Enter Item Number:"))
                if Tiffin_Choice==1:
                    sql_syntax = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                    values =(Enter_username,Tiffin_Choice)
                    cursor.execute(sql_syntax, values)
                    mydb.commit()
                        
                if Tiffin_Choice==2:
                    sql_syntax1 = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                    values1 =(Enter_username,Tiffin_Choice)
                    cursor.execute(sql_syntax1, values1)
                    mydb.commit()
              
                if Tiffin_Choice==3:
                    sql_syntax2 = "INSERT INTO User_TiffinChoice (Username,Tiffin_Choice_Id) VALUES(%s, %s)"
                    values2 =(Enter_username,Tiffin_Choice)
                    cursor.execute(sql_syntax2, values2)
                    mydb.commit()
                
                if Tiffin_Choice==8:
                    break
                
            cursor.execute("""SELECT SUM(b.Cost) FROM User_TiffinChoice a JOIN Tiffin_Type b ON a.Tiffin_Choice_Id=b.Tiffin_Id WHERE a.Username= %s""",(Enter_username , ))
            Total_Cost=cursor.fetchone()
            for cost in Total_Cost:
                print("")
                print("Your Total Cost is:",cost,"Rupees")
                print("")

            print("Enter the corresponding day number to select days on which tiffin is to be delivered")
            print("")
            print("""
                        1 == Monday
                        2 == Tuesday
                        3 == Wednesday
                        4 == Thrusday
                        5 == Friday
                        6 == Saturday
                        7 == Sunday
                        """
                 )

            Day_Choice=0
            cursor.execute("""DELETE FROM User_TiffinDays WHERE Username= %s""",(Enter_username , ))
            while Day_Choice!=8:
                Day_Choice=int(input("Enter Day Number:"))
                if Day_Choice==1:
                    sql_syntax_day1 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day1 =(Enter_username,"Monday")
                    cursor.execute(sql_syntax_day1, values_day1)
                    mydb.commit()

                if Day_Choice==2:
                    sql_syntax_day2 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day2 =(Enter_username,"Tuesday")
                    cursor.execute(sql_syntax_day2, values_day2)
                    mydb.commit() 

                if Day_Choice==3:
                    sql_syntax_day3 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day3 =(Enter_username,"Wednesday")
                    cursor.execute(sql_syntax_day3, values_day3)
                    mydb.commit() 

                if Day_Choice==4:
                    sql_syntax_day4 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day4 =(Enter_username,"Thursday")
                    cursor.execute(sql_syntax_day4, values_day4)
                    mydb.commit() 

                if Day_Choice==5:
                    sql_syntax_day5 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day5 =(Enter_username,"Friday")
                    cursor.execute(sql_syntax_day5, values_day5)
                    mydb.commit() 

                if Day_Choice==6:
                    sql_syntax_day6 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day6 =(Enter_username,"Saturday")
                    cursor.execute(sql_syntax_day6, values_day6)
                    mydb.commit()

                if Day_Choice==7:
                    sql_syntax_day7 = "INSERT INTO User_TiffinDays (Username,Tfiini_Days_Choice) VALUES(%s, %s)"
                    values_day7 =(Enter_username,"Sunday")
                    cursor.execute(sql_syntax_day7, values_day7)
                    mydb.commit()                                   
                
                if Day_Choice==8:
                    break
            
            print("")
            Order_Summary=0
            while Order_Summary!="y":
                Order_Summary=input("Please press y to get your order sumary:")
                if Order_Summary=="y":
                    print("")
                    print("ORDER SUMMARY:")
                    print("")
                cursor.execute("""SELECT Name FROM customer_info
                            WHERE Username= %s""", (Enter_username , ))
                result_name=cursor.fetchone()
                for name in result_name:
                    print("Name:",name)
                cursor.execute("""SELECT Address FROM customer_info
                        WHERE Username= %s""", (Enter_username , ))
                result_address=cursor.fetchone()
                for address in result_address:
                    print("Address:",address)
                cursor.execute("""SELECT Contact FROM customer_info
                        WHERE Username= %s""", (Enter_username , ))
                result_contact=cursor.fetchone()
                for contact in result_contact:
                    print("Contact Number:",contact)
                cursor.execute("""SELECT Email FROM customer_info
                        WHERE Username= %s""", (Enter_username , ))
                result_email=cursor.fetchone()
                for email in result_email:
                    print("Email Address:",email)
                cursor.execute("""SELECT Tiffin_Type.Tiffin_Id,Tiffin_Type.Tiffin,Tiffin_Type.Cost
                            FROM Tiffin_Type
                            INNER JOIN User_TiffinChoice ON
                            Tiffin_Type.Tiffin_Id=User_TiffinChoice.Tiffin_Choice_Id
                            WHERE User_TiffinChoice.Username  = %s""", (Enter_username , ))
                result_selected_orders=cursor.fetchall()
                for orders in result_selected_orders:
                    print("Selected Orders are:",*orders)
                cursor.execute("SELECT Tfiini_Days_Choice FROM User_TiffinDays WHERE Username=%s", (Enter_username , ))
                result_selected_orders_days=cursor.fetchall()
                for days in result_selected_orders_days:
                    print("Selected Days are:",*days)   

            print("")
            OrderConfirmation_Choice=input("Type yes if you want to confirm your orders or press no to exit:")
            if OrderConfirmation_Choice=="yes":
                cursor.execute("""SELECT User_Id FROM customer_info WHERE Username = %s""", (Enter_username , ))
                result_ID=cursor.fetchone()
                for ID in result_ID:
                    Customer_ID=ID
                today = date.today()    
                formatted_date = today.strftime('%Y-%m-%d')    
                sql_syntax3= "INSERT INTO Delivery_info (Customer_ID ,TiffinBoy_Name,TiffinBoy_Phone_Number,Delivery_Address ,Customer_Contact,Customer_Name,Order_Status,Order_Days,DeliverOrder_Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values3 =(Customer_ID,'Arun Singh',9893498910,address,contact,name,'Booked','User Chosen Days',formatted_date)
                cursor.execute(sql_syntax3,values3)
                mydb.commit()

                sql_syntax_sum= "INSERT INTO User_TotalCost (User_cost,Username) VALUES(%s,%s)"
                values_sum=(cost,Enter_username)
                cursor.execute(sql_syntax_sum,values_sum)
                mydb.commit()
                
                cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Customer_ID = %s""", (ID , ))
                result_orderid=cursor.fetchone()
                for print_orderid in result_orderid:
                    show_orderid=print_orderid
                print("")
                print("Ordered Successfully!!")
                print("")
                print("Your Order ID is:",show_orderid)
                exit()
                
            if OrderConfirmation_Choice=="no":
                    
                exit()
            
        if option_selection==2:
            order_id_input=int(input("Enter Your Order ID:"))
            cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Order_ID = %s  """ , (order_id_input , ))
            result_order_id_output=cursor.fetchone()
            if result_order_id_output==None:
                print("OrderID entered is incorrect Please restart the program")
                exit()
            for orderid_forchecking in result_order_id_output:
                orderid_data=orderid_forchecking
            if order_id_input==orderid_data:
                cursor.execute("""SELECT Order_Status FROM Delivery_info
                            WHERE Order_ID= %s""", (order_id_input , ))
                result_Order_Status=cursor.fetchone()
                for Order_Status in result_Order_Status:
                    print("Tiffin Status:",Order_Status)
                cursor.execute("""SELECT DeliverOrder_Date FROM Delivery_info
                            WHERE Order_ID= %s""", (order_id_input , ))
                result_DeliverOrder_Date=cursor.fetchone()
                for DeliverOrder_Date in result_DeliverOrder_Date:
                    print("Tiffin Booking Date:",DeliverOrder_Date)
                    exit()

        if option_selection==3:
            order_id_input1=int(input("Enter Your Order ID:"))
            cursor.execute("""SELECT Order_ID FROM Delivery_info WHERE Order_ID = %s  """ , (order_id_input1 , ))
            result_order_id_output1=cursor.fetchone()
            if result_order_id_output1==None:
                print("OrderID entered is incorrect or you have not booked any tiffin Please restart the program")
                exit()
            for orderid_forchecking1 in result_order_id_output1:
                orderid_data1=orderid_forchecking1
            if order_id_input1==orderid_data1:
                print("TIFFIN & BILLING DETAILS:")
                print(" ")
                cursor.execute("""SELECT Name FROM customer_info
                                WHERE Username= %s""", (Enter_username , ))
                result_name1=cursor.fetchone()
                for name1 in result_name1:
                    print("Name:",name1)
                cursor.execute("""SELECT Address FROM customer_info
                            WHERE Username= %s""", (Enter_username , ))
                result_address1=cursor.fetchone()
                for address1 in result_address1:
                    print("Address:",address1)
                cursor.execute("""SELECT Contact FROM customer_info
                            WHERE Username= %s""", (Enter_username , ))
                result_contact1=cursor.fetchone()
                for contact1 in result_contact1:
                    print("Contact Number:",contact1)
                cursor.execute("""SELECT Email FROM customer_info
                            WHERE Username= %s""", (Enter_username , ))
                result_email1=cursor.fetchone()
                for email1 in result_email1:
                    print("Email Address:",email1)
                cursor.execute("""SELECT Tiffin_Type.Tiffin_Id,Tiffin_Type.Tiffin,Tiffin_Type.Cost
                            FROM Tiffin_Type
                            INNER JOIN User_TiffinChoice ON
                            Tiffin_Type.Tiffin_Id=User_TiffinChoice.Tiffin_Choice_Id
                            WHERE User_TiffinChoice.Username  = %s""", (Enter_username , ))
                result_selected_orders1=cursor.fetchall()
                for orders1 in result_selected_orders1:
                    print("Selected Orders are:",*orders1)
                cursor.execute("SELECT Tfiini_Days_Choice FROM User_TiffinDays WHERE Username=%s", (Enter_username , ))
                result_selected_orders_days=cursor.fetchall()
                for days in result_selected_orders_days:
                    print("Selected Days are:",*days)
                    
                cursor.execute("""SELECT User_cost FROM User_TotalCost WHERE Username=%s""", (Enter_username , ))
                result_cost_user=cursor.fetchone()
                for TOTAL_COST in result_cost_user:
                    print("Your Total Cost is:",TOTAL_COST,"Rupees")
                        
                print("Tfffin Delivery Details:")
                print(" ")
                cursor.execute("""SELECT TiffinBoy_Name FROM Delivery_info
                                WHERE Order_ID= %s""", (order_id_input1 , ))
                result_tiffinboyname=cursor.fetchone()
                for tiffinboyname in result_tiffinboyname:
                        print("Tiffin Boy Name:",tiffinboyname)
                          
                cursor.execute("""SELECT TiffinBoy_Phone_Number FROM Delivery_info
                                WHERE Order_ID= %s""", (order_id_input1 , ))
                result_tiffinboyphone=cursor.fetchone()
                for tiffinboyphone in result_tiffinboyphone:
                    print("Tiffin Boy Phone No:",tiffinboyphone)
            exit()
        if option_selection==6:
            Enter_master_username=input("Enter Master UserName:")
            Enter_master_Password= getpass.getpass("Enter Master Password:")
            cursor.execute("""SELECT Master_Password FROM Master_Login
                        WHERE Master_Username= %s""", (Enter_master_username , ) )
            result_master=cursor.fetchone()
            if result_master==None:
                print("Master Username entered is incorrect")
                exit()
            for row_master in result_master:
                Data_master=row_master

            cursor.execute("""SELECT Master_Username FROM Master_Login
                    WHERE Master_Password= %s""", (Enter_master_Password , ) )
            result1_master=cursor.fetchone()
            if result1_master==None:
                print("Master Password entered is incorrect")
                exit()
            for row1_master in result_master:
                Data1_master=row1_master
                if Data_master==Enter_master_Password:
                    print("LogIn Successful")
                    print("COMPANY STATISTICS ARE:")
                    cursor.execute("SELECT SUM(b.Cost) FROM User_TiffinChoice a JOIN Tiffin_Type b ON a.Tiffin_Choice_Id=b.Tiffin_Id")
                    result_totalsale=cursor.fetchone()
                    for resulttotalsale in result_totalsale:
                        print("Total Sale:",resulttotalsale)
                    cursor.execute("SELECT COUNT(User_ID) AS NumberofAccounts FROM customer_info")
                    result_totalaccount=cursor.fetchone()
                    for resulttotalaccount in result_totalaccount:
                        print("Account Count:",resulttotalaccount)
                    cursor.execute("SELECT COUNT(Order_ID) AS NumberofCustomers FROM Delivery_info")
                    result_totalcustomers=cursor.fetchone()
                    for resulttotalcustomers in result_totalcustomers:
                        print("Customer Count:",resulttotalcustomers)
                    average=resulttotalsale/resulttotalcustomers
                    print("Averge Tiffin Order Cost:",average)
            
        if option_selection==5:
            delete_tiffinsubscription=input("Do You reall want to unsubscribe to the tiffin service with Username " + str(Enter_username) + " (yes/no):")
            if delete_tiffinsubscription=="yes":
                cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                result_for_userid=cursor.fetchone()
                for finalresult_userid in result_for_userid:
                    finalresult1_userid=finalresult_userid
                    delete_statement= """DELETE FROM User_TiffinChoice WHERE Username=%s"""
                    cursor.execute(delete_statement, (Enter_username,))
                    mydb.commit()
                    delete_statement1= """DELETE FROM Delivery_info WHERE Customer_ID=%s"""
                    cursor.execute(delete_statement1, (finalresult1_userid,))
                    mydb.commit()
                    delete_statement2= """DELETE FROM User_TiffinDays WHERE Username=%s"""
                    cursor.execute(delete_statement2, (Enter_username,))
                    mydb.commit()
                    print("Tfffin service unsubscribed")
                    exit()
                exit()
            if delete_tiffinsubscription=="no": 
                exit()
        if option_selection==4:
            print(" What Do You Want To Update ? Press the corresponding number to navigate WARNING! You can update only one detail at a time please restart the programm to update multiple details")
            print("""
                        1 == Name
                        2 == Address
                        3 == Contact
                        4 == Email Address
                        """
                 )
            update_user_choice=int(input("Enter the Number:"))
            if update_user_choice==1:
                new_name=input("Enter New Name:")
                newname_statement= """UPDATE customer_info SET Name=%s WHERE Username =%s"""
                values_name=(new_name,Enter_username)
                cursor.execute(newname_statement, values_name)
                cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                result_for_userid1=cursor.fetchone()
                for finalresult_userid1 in result_for_userid1:
                    finalresult1_userid1=finalresult_userid1
                newname_statement1= """UPDATE Delivery_info SET Customer_Name=%s WHERE Customer_ID =%s"""
                values_name1=(new_name,finalresult1_userid1)
                cursor.execute(newname_statement1, values_name1)
                mydb.commit()
                print("Name Updated Successfully")
                    
            if update_user_choice==2:
                new_address=input("Enter New Address:")
                newaddress_statement= """UPDATE customer_info SET Address=%s WHERE Username =%s"""
                values_address=(new_address,Enter_username)
                cursor.execute(newaddress_statement, values_address)
                cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                result_for_userid2=cursor.fetchone()
                for finalresult_userid2 in result_for_userid2:
                    finalresult1_userid2=finalresult_userid2
                newaddress_statement1= """UPDATE Delivery_info SET Delivery_Address=%s WHERE Customer_ID =%s"""
                values_address1=(new_address,finalresult_userid2)
                cursor.execute(newaddress_statement1, values_address1)
                mydb.commit()
                print("Address Updated Successfully")
                    
            if update_user_choice==3:
                new_contact=int(input("Enter New Contact:"))
                newcontact_statement= """UPDATE customer_info SET Contact=%s WHERE Username =%s"""
                values_contact=(new_contact,Enter_username)
                cursor.execute(newcontact_statement, values_contact)
                cursor.execute("""SELECT (User_Id) FROM customer_info WHERE Username= %s""", (Enter_username , ))
                result_for_userid3=cursor.fetchone()
                for finalresult_userid3 in result_for_userid3:
                    finalresult1_userid3=finalresult_userid3
                newcontact_statement1= """UPDATE Delivery_info SET Customer_Contact=%s WHERE Customer_ID =%s"""
                values_contact1=(new_contact,finalresult_userid3)
                cursor.execute(newcontact_statement1, values_contact1)
                mydb.commit()
                print("Contact Updated Successfully")

            if update_user_choice==4:
                new_mail=input("Enter New Email Address:")
                newmail_statement= """UPDATE customer_info SET Email=%s WHERE Username =%s"""
                values_mail=(new_mail,Enter_username)
                cursor.execute(newmail_statement, values_mail)
                mydb.commit()
                print("Email Address Updated Successfully")
        exit()
        