
# Importing libraries
from selenium import webdriver  # Tool for automationh
import time  # Get time and sleep

# Enter your Username and Password here to login
username = input('Enter you Github Username to start session: ')
password = input('And password to start session: ')

# Run our driver to initiate session
# exectable_path is the path where our chrome driver is installed
# Can be downloaded from the link: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(executable_path='C:/Users/chromedriver.exe')

# Get request to the Github URL to login
driver.get('https://github.com/login')

# Finding the 'Enter Username' space and sending keys to enter
btn = driver.find_element_by_name('login')
btn.send_keys(username)

# Finding the 'Enter Password' space and sending keys to enter
btn = driver.find_element_by_name('password')
btn.send_keys(password)

# Finding Submit button and clicking on it to finally login to your account
btn = driver.find_element_by_name('commit')
btn.click()


# Get to your Profile page
driver.get(f'https://github.com/{username}')

# These are some popular usernames across whole Github
# If you wish to follow all the followers of any user(s) for your choice,
# just add them in the below list at the starting
users = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon",
         "mattt", "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig", "mojombo",
         "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
         "josevalim", "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
         "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub", "BYVoid", "laruence",
         "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger", "cloudwu",
         "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
         "pjhyett", "dhh", "gaearon"]

# Iterating over all the usernames
for user in users:

    # Counter to take to next -> next pages
    t = 0

    # Looping through all the followers pages of username 'user' from page 1 to last
    while True:

        # Incrementing counter to reach next page after completing task on the current page
        t += 1

        # URL for the page to load
        string = f"https://github.com/{user}?page={t}&tab=followers"

        # Requesting to the page and starting task
        driver.get(string)

        # Waiting for the page to load properly
        time.sleep(1)

        # Finding all the follow buttons present on the current page
        follow_buttons = driver.find_elements_by_name('commit')[0::2]  # 0 -> To Follow, 1 -> To Unfollow

        # Condition to check if we reached the last page, if so then break
        if len(follow_buttons) < 25:
            break

        # Looping through al the follow buttons
        for button in follow_buttons:
            # Clicking on the buttons
            button.submit()

        # Waiting to follow and save all the users present on the page
        time.sleep(1)

    # If you wish to just do this for only the first user in the above list, user break here.
    # break
driver.quit()