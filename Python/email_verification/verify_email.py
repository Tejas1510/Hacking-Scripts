# This script checks whether the email address is existing or not.
# Using Python 3
import socket
import smtplib

# Getting local server hostname
host = socket.gethostname()

# SMTP lib setup
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('me@domain.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Failed')