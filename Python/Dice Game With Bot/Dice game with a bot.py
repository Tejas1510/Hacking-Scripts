import random
import time as t


def actions(choice):
    h_sum=b_sum=0
    print("Start playing the game now")
    t.sleep(1)
    for die in range(0,choice):
        person=random.randint(1,6)
        t.sleep(1)
        print("human got",person)
        h_sum+=person
    t.sleep(1)
    print("Total sum of human is:",h_sum)
    t.sleep(1)
    print("Now its time for the bot")
    t.sleep(1)
    for die in range(0,choice):
        bot=random.randint(1,6)
        t.sleep(1)
        print("Bot got",bot)
        b_sum+=bot
    t.sleep(1)
    print("Total sum  of bot is:", b_sum)
    t.sleep(2)

    total="\n Human won" if h_sum>b_sum else  "\nBot won" if h_sum<b_sum else"Its a tie"
    print(total)
    t.sleep(1)

def play():
  die=0
  rolling=""
  while die==0:
      choice=int(input("How many times you wamt to  be rolled?? (1-5)"))
      if choice>0and choice<6:
          actions(choice)
          break
      else:
          print("Please enter the correct choice")
  print("Do you want to continue the game??")
  while rolling!="Yes":
     rolling=input().lower().capitalize()
     if rolling=="Yes":
      play()
     else:
         print("It was wonderful playing with a bot")
     break
play()
