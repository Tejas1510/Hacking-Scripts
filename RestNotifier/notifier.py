import webbrowser
import time


breaks = int(input("How many breaks do you wish to take? : "))
break_count = 0
break_time=int(input("Enter after how much time you want a break in min (Minimum 1 min) : "))
choice = input("Would you love to hear a mediation song in the break?\n Enter Y for yes and N for No : ")
if(break_count<breaks):
    time.sleep(break_time*60)
    if(choice=="Y"):
        webbrowser.open("https://www.youtube.com/watch?v=Pw3mhrf7Uuo")
        break_count = break_count+1
    else:
        print("Please Take a break and have a walk")
        break_count = break_count+1

if(break_count==1):
    while(break_count<breaks):
        time.sleep(break_time*60)
        if(choice=="Y"):
            webbrowser.open("https://www.youtube.com/watch?v=Pw3mhrf7Uuo")
            break_count = break_count+1
        else:
            print("Please Take a break and have a walk")
            break_count = break_count+1


else:
    exit
