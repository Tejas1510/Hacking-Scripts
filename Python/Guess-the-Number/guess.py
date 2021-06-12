#library for getting a random number
import random
import math
num = random.randint(0, 20)

num1 =random.randint(3,6)  # for number of chances. i am taking the number which should be greater than or equal to 3 to make user friendly game 

print("--Welcome to Guess The Number Game--")
print("\n you have " + str(num1) + " chances to guess the number")
count = 0
# Iterate using while loop
while count < num1:
    count += 1
    res = int(input("Please input a number between 0 and 20:"))
    try:
        val = int(res)
    except ValueError:
        print("This is not a valid integer. Please try again!")
        continue
    # Check whether the user input is high or low than the random number generated.
    if val < num:
        print("This is lower than actual number. Please try again!")
    elif val > num:
        print("This is higher than actual number. Please try again!")
    else:
        # Final result will be printed with this message as the user input matches the random number generated
        print("Hurray! you won, this is the correct number🥳")
        exit(0)
        guessCheck = "correct"
if (count >= num1):
   print("the number is "+ str(num)+" and you loose the game ☹️")        
print("Thank you for playing Guess The Number. See you again!")
