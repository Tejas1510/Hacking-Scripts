import random
list=["s","p","sc"] 
choice = random.choice(list)

print("s for stone\n")
print("p for paper\n")
print("sc for scicors\n")
print("choose any one from this\n")

user_point = 0
computer_point = 0

number_of_attempts = 1
while (number_of_attempts < 11) :
  choice = random.choice(list)
  a=str(input())
  if (a == "s" and choice == "p") :
    print("The computer used paper, so you lost")

  elif (a == "s" and choice == "sc") :
    print("The computer used scicors, so you win")
  
  elif (a == "p" and choice == "s") :
    print("The computer used stone, so you win")
  
  elif (a =="p" and choice == "sc") :
    print("The computer used scicors, so you lost")
  
  elif (a == "sc" and choice == "s") :
    print("The computer used stone, so you lost") 
  
  elif (a == "sc" and choice == "p") :
    print("The computer used paper, so you win")
  
  elif(a== choice):
        print("You and computer used same")
  
  else :
        print("Invalid statement please try again")
        exit
  
  number_of_attempts = number_of_attempts + 1
  
  print("Number of attempts remaining",11-number_of_attempts)

  if (a == "s" and choice == "sc" or a == "p" and choice == "s" or a == "sc" and choice == "p") :
    user_point = user_point + 1
   

  elif(a == "s" and choice == "p" or a =="p" and choice == "sc" or a == "sc" and choice == "s") :
    computer_point = computer_point + 1

  else :
    user_point = user_point
    computer_point = computer_point
  print(f"Your score is {user_point} and computer score is {computer_point}")

if (user_point > computer_point) :
      print("You won the match")
else :
      print("You lost the match")

