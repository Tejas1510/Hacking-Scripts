-- To create database named "project" for the tiffin booking system
CREATE DATABASE project; 
 
 -- Using our created database project
USE project;

-- This will drop any table named customer_info without giving errors
-- Run the drop command of this table at the end start droping from Tiffin_Type table as this table has foreign key constraints
DROP TABLE if exists customer_info; 

-- Creating required tables (customer_info)
CREATE TABLE customer_info (
User_Id            int(10) AUTO_INCREMENT NOT NULL Primary key,
Name               char(100),
Address            char(150),
Contact            varchar(10),
Email              char(150),
Username           char(50) unique,
Create_Password    char(100)
);

-- This will drop any table named Tiffin_Type without giving errors 
DROP TABLE if exists Tiffin_Type;

-- Creating required tables (Tiffin_Type)
CREATE TABLE Tiffin_Type(
Tiffin_Id     int(10) AUTO_INCREMENT NOT NULL Primary key ,
Tiffin        char(100),
Cost          int(10)
);

-- Inserting the table with cost values which will be used to calculate the user's total cost
INSERT INTO Tiffin_Type(Tiffin,Cost) VALUES("Breakfast",120),("Lunch",180),("Dinner",300);

-- This will drop any table named User_TiffinChoice without giving errors 
DROP TABLE if exists User_TiffinChoice;

-- Creating required tables (User_TiffinChoice)
CREATE TABLE User_TiffinChoice(
Username char(50),
Tiffin_Choice_Id int(10),
FOREIGN KEY (Username)   REFERENCES     customer_info(Username)
);

-- This will drop any table named User_TiffinDays without giving errors
DROP TABLE if exists User_TiffinDays;

-- Creating required tables (User_TiffinDays)
CREATE TABLE User_TiffinDays(
Username char(50),
Tfiini_Days_Choice char(50),
FOREIGN KEY (Username)   REFERENCES     customer_info(Username)
);

-- This will drop any table named User_TotalCost without giving errors
DROP TABLE if exists User_TotalCost;

-- Creating required tables (User_TotalCost)
CREATE TABLE User_TotalCost(
User_cost int(100),
Username char(50),
FOREIGN KEY (Username)   REFERENCES     customer_info(Username)
);

-- For delivery details

-- This will drop any table named Delivery_info without giving errors
DROP TABLE if exists Delivery_info;

-- Creating required tables (Delivery_info)
CREATE TABLE Delivery_info (
 Order_ID                   int(4) auto_increment not null primary key,
 Customer_ID                INT(10),
 TiffinBoy_Name             CHAR(150),
 TiffinBoy_Phone_Number     VARCHAR(10),
 Delivery_Address           CHAR(200),
 Customer_Contact           VARCHAR(10),
 Customer_Name              CHAR(200),
 Order_Status               CHAR(100),
 Order_Days                 CHAR(200),
 DeliverOrder_Date          date,
 FOREIGN KEY(Customer_ID)   REFERENCES     customer_info(User_Id)
 );
 
 -- This will drop any table named Master_Login without giving errors
DROP TABLE if exists Master_Login;
 
 -- Creating required tables (Master_Login)
 CREATE TABLE Master_Login
 (Master_User_ID     int(10) auto_increment primary key,
  Master_Username    char(200),
  Master_Password    char(200)
 );
 
 -- Inserting the values in Master_Login ,here use you own username and password near ('create_username','create_password') and if you dont change then the default username and password will be create_username and create_password respectively
 INSERT INTO Master_Login (Master_Username,Master_Password)VALUES('create_username','create_password'); 
 
 -- By running the below statement you can check that the username and the password is successfully inserted in the Master_Login table
 SELECT * FROM Master_Login;
 SHOW TABLES;
 