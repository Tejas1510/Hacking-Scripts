try:
    import pandas as pd
    import smtplib
    import re
    import os
except ImportError:
    print("\n some modules are not installed\n installing them for you :-)")
    cmd = "pip install pandas"
    cmd1 = "pip install smtplib"
    cmd2 = "pip install openpyxl"
    os.system(cmd)
    os.system(cmd1)
    os.system(cmd2)

# input...........
SenderAddress = input("your email :  ").strip()
print(
    "\nplease allow 'enable less secured apps ' option on this account to send emails\n"
)
password = input("your password : ").strip()
# ...........

# using pandas and openpyxl for reading from email.xlsx  and setting up smtp server
e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(SenderAddress, password)
except smtplib.SMTPAuthenticationError:
    print(
        "\n[+]Username or password not accepted or not enabled less secured apps on the above Mail account \n"
    )

subject = "Hi there"

# reading subject from msg.txt....

a_file = open("msg.txt")
lines = a_file.readlines()

msg = ""
for line in lines:
    msg = msg + line
a_file.close()
# ..........

body = "Subject: {}\n\n{}".format(subject, msg)
# ........send mail.....

try:
    for email in emails:
        server.sendmail(SenderAddress, email, body)
    server.quit()
    print("\nemail successully sent to :\n")
    for mail in emails:
        print(mail + "\n")

except smtplib.SMTPSenderRefused:
    print("\n[+] could not send emails :-( ")
