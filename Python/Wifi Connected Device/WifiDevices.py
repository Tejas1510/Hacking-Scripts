import subprocess

connected = subprocess.check_output(["netsh", "wlan", "show", "network"])
connected = connected.decode("ascii")
connected = connected.replace("\r", "")
ls = connected.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)
print("\n")
# Contributed by: Anubhab
