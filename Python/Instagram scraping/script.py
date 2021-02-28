from selenium import webdriver
from time import sleep


class instaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.instagram.com")
        sleep(3)

        self.username = username
        self.password = password

        usernamefield = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        usernamefield.send_keys(username)

        passwordfield = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        passwordfield.send_keys(password)

        loginbtn = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]')
        loginbtn.click()
        sleep(10)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        sleep(5)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div').click()

        sleep(5)

    def get_unfollowers(self):

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self.get_names()

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self.get_names()

        not_following_back = [
            user for user in following if user not in followers]

        print("Information Collection Successful .....\n")
        print('Writing usernames to "listfile.txt" ......\n')

        with open('listfile.txt', 'w') as filehandle:
            for listitem in not_following_back:
                filehandle.write('%s\n' % listitem)

        self.driver.quit()

        print("Successful......")

    def get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]')

        last_ht, ht = 0, 1

        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        links = self.driver.find_elements_by_tag_name('a')
        all = [name.text for name in links if name.text != '']

        self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

        trash = ['Edit Profile', 'POSTS', 'IGTV', 'SAVED', 'TAGGED', 'ABOUT', 'HELP',
                 'PRESS', 'API', 'JOBS', 'PRIVACY', 'TERMS', 'LOCATIONS', 'TOP ACCOUNTS', 'HASHTAGS']

        del all[0:int(len(trash))]
        return all


def main():

    print("Welcome to Instagram bot !\n")

    username = str(input("Enter your Instagram username : "))
    password = str(input("Enter your Instagram passwword : "))
    print("\n")

    try:
        myBot = instaBot(username, password)
        myBot.get_unfollowers()

    except:
        print("Something went wrong ! .....")


main()
