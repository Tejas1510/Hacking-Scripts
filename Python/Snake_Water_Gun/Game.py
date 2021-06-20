# Snake, Water, Gun Game
print("WELCOME TO SNAKE, WATER, GUN game")
import random

computer_point = 0
your_point = 0
count = 1

list = ["Snake", "Water", "Gun"]

while(count <= 10):
    print("Press 's' for snake,'w' for water,'g' for gun")
    a = input()
    choice = random.choice(list)
    print("PC chose", choice)
    
    if(a == choice):
        print("Tie so nobody gets a point")

    elif(a == 's' and choice == "Water"):
        your_point = your_point+1
        print("You got", your_point, "point")

    elif (a == 's' and choice == "Gun"):
        computer_point = computer_point + 1
        print("PC got", computer_point, "point")

    elif (a == 'w' and choice == "Gun"):
        your_point = your_point + 1
        print("You got", your_point, "point")

    elif (a == 'w' and choice == "Snake"):
        computer_point = computer_point + 1
        print("PC got", computer_point, "point")

    elif (a == 'g' and choice == "Snake"):
        your_point = your_point + 1
        print("You got", your_point, "point")

    elif (a == 'g' and choice == "Water"):
        computer_point = computer_point + 1
        print("PC got", computer_point, "point")

    count = count+1

print("\nChances over!!")

if (computer_point > your_point):
    print("\nPC won the game...Better luck next time!!")

else:
    print("Congo!! You won the game")
