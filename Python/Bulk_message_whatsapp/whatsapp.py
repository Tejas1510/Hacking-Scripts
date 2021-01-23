import pywhatkit
p=input("Enter the number with country code eg.'+91*********' ,Don't Forget to add the country code with a + :")
q=input("PLease enter the message you want to send to the receiver : ")
Time=int(input('Enter the Hour : '))
Time2=int(input('Enter the Minutes : '))

pywhatkit.sendwhatmsg(p,q,Time,Time2)