import math
import random
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

#first question

print("You are on a muddy road, it has come to an end and you can go left or right\n")
answer  = input("Which way would you like to go? left or right! please provide a appropriate input else you will loose ").lower()

# if left was answered
if answer == "left":
    answer = input("You come to a river, you can walk around the river  or swim accross the river?\n Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an crocodile.")
    elif answer == "walk":
        print("good move boy\n")
        answer = input("now tell which direction you will choose")
        if answer == "left":
           print("there is a devil\n")
           answer = input("What will you do fight or go back").lower()
           if answer == "back":
             print("hey you are a fearful guy! you loose")
           elif answer  == "fight":
             m = random.randint(0,1)
             if (m == 0):
               print("devil won and you died" + name + "but you are courageous")
             else:
               print("wow " + name + " you won . you are damn strong and courageous.so you won man")    
    else:
        print('Not a valid option. You lose.')

#if right was answered
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?\n")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger which has weapons. Do you talk to them (yes/no)?\n ")

        if answer == "yes":
            print("Ya They are the nice strangers .You talk to the stanger and they tell you the exact direction where you want to go. You WIN!")
        elif answer == "no":
            answer = input("You ignore the stranger,\n" + "you are damn shy person . Ok leave! now in which direction you will go left or right\n").lower()
            if answer == "left":
              print("you went to the opposite direction start the game again" ,name)
            else:
              print("now" + name +  "last end ,one direction is correct and one will lead to death choose wisely")
              print("Decide by tossing the coin head is right and tail is left")
              k = random.randint(0,1)
              if(k == 0):
                print("its head better go right and pray to god that it is correct")
              else:
                print("its tail go left pray to god that it is correct")
              answer  = input("enter the direction").lower()
              
              if (answer == "right"):
                 print("hurray you reached to the right location",name) 
              else:
                 print("you lost",name)    
        else:
            print('Not a valid option. You lose.')
            
    else:
        print('Not a valid option. You lose.')

#if something else was answered then showing invalid
else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)

