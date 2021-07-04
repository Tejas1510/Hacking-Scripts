# 21 Number Game

# returns the nearest multiple of 4
def nearestmul4(n):
    if n>=4:
        near=n+(4-(n%4))
    else:
        near=4
    return near

def lose1():
    print("OOPS! You lost the game.\n")
    print("Try another time!")
    exit(0)

# check whether the numbers are consecutive or not
def check(xyz):
    i=1
    while i<len(xyz):
        if(xyz[i]-xyz[i-1]!=1):
            return False
        i=i+1
    return True 

# starts the game
def start1():
    string1=[]
    last=0
    while True:
        print("Enter F to play the first chance or S to play the second chance:")
        chance=input("> ")

        # if player choose F
        if chance=='F':
            while True:
                if last==20:
                    lose1()
                else:
                    print("Your turn :\n")
                    print("How many numbers you wish to put:")
                    inp=int(input("> "))

                    if inp>0 and inp<=3:
                        comp=4-inp
                    else:
                        print("oops! Wrong input.\n")
                        print("You are disqualified!")
                        lose1()
                
                    i,j=1,1
                    print("Now enter the values:")
                    while i<=inp:
                        a=input("> ")
                        a=int(a)
                        string1.append(a)
                        i=i+1
                
                    last=string1[-1]

                    if check(string1)==True:
                        if last==21:
                            lose1()
                        else:
                            while j<=comp:
                                string1.append(last+j)
                                j=j+1
                            print("Order of inputs after computer's turn is: ")
                            print(string1)
                            last=string1[-1]
                    else:
                        print("You did not input consecutive integers!")
                        lose1()

        # if player choose S
        elif chance=='S':
            comp=1
            last=0
            while last<20:
                j=1
                while j<=comp:
                    string1.append(last+j)
                    j=j+1
                print("order of inputs after computer's turn is: ")
                print(string1)
                if string1[-1]==20:
                    lose1()
                else:
                    print("Your turn :\n")
                    print("How many numbers you wish to put:")
                    inp=int(input("> "))
                    inp=int(inp)
                    i=1
                    print("Enter your values:")
                    while i<=inp:
                        string1.append(int(input("> ")))
                        i=i+1
                    last=string1[-1]
                    if check(string1)==True:
                        near=nearestmul4(last)
                        comp=near-last
                        if comp==4:
                            comp=3
                        else:
                            comp=comp
                    else:
                        print("OOPS! You did not input consecutive integers.")
                        lose1()
            print("!!!Congratulations!!!")
            print("Hurray! You won the game!")
            exit(0)
        else:
            print("Wrong choice...please choose F or S")

# driver code
game=True
while game==True:
    print("Player 2 is computer.")
    print("Do you want to play the game (yes/no)")
    ans=input("> ")
    if ans=='yes':
        start1()
    else:
        print("Do you want to exit from the game(yes/no)")
        nex=input("> ")
        if nex=='yes':
            print("You are quitting the game...")
            exit(0)
        elif nex=='no':
            print("continuing...")
        else:
            print("Wrong choice!")
