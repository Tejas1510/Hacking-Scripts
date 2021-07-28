import sys
import random
import time

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (type 'exit' to quit)\n ")
    
    answers = random.randint(1,21)
    
    if question == "exit":
        sys.exit()
    
    elif answers == 1:
        print("\nShaking...\n")
        time.sleep(1)
        print("\nIt is certain\n")
    
    elif answers == 2:
        time.sleep(1)
        print("\nAs I see it, yes.\n")
    
    elif answers == 3:
        time.sleep(1)
        print ("\nReply hazy, try again.\n")
    
    elif answers == 4:
        time.sleep(1)
        print ("\nDon't count on it.\n")
    
    elif answers == 5:
        time.sleep(1)
        print ("\nIt is decidedly so.\n")
    
    elif answers == 6:
        time.sleep(1)
        print ("\nMost likely.\n")
    
    elif answers == 7:
        time.sleep(1)
        print ("\nAsk again later.\n")
    
    elif answers == 8:
        time.sleep(1)
        print ("\nMy reply is no.\n")
    
    elif answers == 9:
        time.sleep(1)
        print ("\nWithout a doubt\n")

    elif answers == 10:
        time.sleep(1)
        print ("\nOutlook good.\n")

    elif answers == 11:
        time.sleep(1)
        print ("\nBetter not tell you now.\n")

    elif answers == 12:
        time.sleep(1)
        print ("\nMy sources say no\n")

    elif answers == 13:
        time.sleep(1)
        print ("\nYes definitely.\n")

    elif answers == 14:
        time.sleep(1)
        print ("\nYes.\n")

    elif answers == 15:
        time.sleep(1)
        print ("\nCannot predict now.\n")

    elif answers == 16:
        time.sleep(1)
        print ("\nOutlook not so good.\n")

    elif answers == 17:
        time.sleep(1)
        print ("\nYou may rely on it.\n")

    elif answers == 18:
        time.sleep(1)
        print ("\nSigns point to yes.\n")

    elif answers == 19:
        time.sleep(1)
        print ("\nPlease go away.\n")

    elif answers == 20:
        time.sleep(1)
        print ("\nVery doubtful.\n")
