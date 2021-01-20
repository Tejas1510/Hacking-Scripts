# Loading Modules
from selenium import webdriver
import time
import getpass

login_url = 'https://www.facebook.com/login.php'

email = input("Enter your email address: ")
password = getpass.getpass("Enter your password: ")


def login(email, password):
    driver = webdriver.Chrome("./")
    driver.get(login_url)
    time.sleep(1)
    # Entering Email Address
    email_input = driver.find_element_by_id('email')
    email_input.send_keys(email)
    # Entering Password
    password_input = driver.find_element_by_id('pass')
    password_input.send_keys(password)
    # Clicking Login Button
    login_button = driver.find_element_by_id('loginbutton')
    login_button.click()
    time.sleep(2)


if __name__ == '__main__':
    login(email, password)
