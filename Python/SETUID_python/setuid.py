
# importing os module
import os
import pty
# Get the real user ID
# of the current process
# using os.getuid() method
uid = os.getuid()

# Print the real user ID
# of the current process
print("Real user ID of the current process:", uid)

# Set real user ID
# of the current process
# using os.setuid() method
uid = int(input("Enter UID: "))
os.setuid(uid)
print("Real user ID changed")


# Print the real user ID
# of the current process
print("Real user ID of the current process:", os.getuid())
pty.spawn('/bin/bash')