import re
p = input("Please enter a passowrd for checking its Strenght : ")
count=0
if(len(p)>=6):
    count=count+1
if(re.search("[a-z]",p)):
    count=count+1
if(re.search("[A-Z]",p)):
    count=count+1
if(re.search("[$#@]",p)):
    count=count+1
if(re.search("[0-9]",p)):
    count=count+1
if(count==1):
    print("The Password is Poor")
elif(count==2):
    print("The Password is Fair")
elif(count==3):
    print("The Password is Good")
elif(count==4):
    print("The Password is Strong")
elif(count==5):
    print("The Password is Very Strong")
else:
    print("INVALID PASSWORD")
