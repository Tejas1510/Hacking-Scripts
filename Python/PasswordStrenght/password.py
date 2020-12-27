import re
p = input("Please enter a passowrd for checking its Strenght : ")

password_strength_check(p):
    length=len(p)
    count=0
    if length < 6:
        return 1
    else:
        if 8<length <10:
            count+=1
        elif length <12:
            count+=2
        elif length <14:
            count+=3
        else:
            count+=4

        if(re.search("[a-z]",p)):
            count=count+1
        if(re.search("[A-Z]",p)):
            count=count+1
        if(re.search("[$#@]",p)):
            count=count+1
        if(re.search("[0-9]",p)):
            count=count+1
    return count

pass_strength = {1:"very weak", 2:"weak", 3:"fair", 4:"strong"}

try:
    print("Your password is", pass_strength[count])
except:
    print("Your password is very strong")
