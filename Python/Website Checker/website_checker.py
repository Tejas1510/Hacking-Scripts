import requests

web = input("Enter website url: ")
response = requests.get(web)

##print the html structure of website
print(response.text)
##sending requests to website
if (response.status_code == 200):
    response = requests.get(web+'/admin.php')

    if(response.status_code == 200):
        print("Vulnerable")
    else:
        print("Non-vulnerable")

else:
    print("Failure")