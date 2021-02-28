import urllib.request
import json

ip = input("Just press enter key to get location of your current IP \n OR \n Enter IP address to get its location and other info:")

resp = urllib.request.urlopen("http://www.ip-api.com/json/"+ip +
                              "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query").read()
resp_dic = json.loads(resp)

print("\n")

for key, value in resp_dic.items():
    print(f"{key} : {value}")
