import subprocess ## to know more about subprocess please refer readme file where i have explained the details about it
wififinalData = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
finalData = wififinalData.decode('utf-8', errors ="backslashreplace")
finalData = finalData.split('\n')
allWifiName = []
for i in finalData:
    if "All User Profile" in i :
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        allWifiName.append(i)
print("Your System is Connected to following wifi networks : ")
i=1
for name in allWifiName:
    print(i,")",name)
    i=i+1
