
'''

In this code, I haven't used any packages and didn't import anything.
Just wrote code by creating function and main interface

Description of each function :
insertLetter(letter, pos) ---> This function takes two arguments letter (either 'O' or 'X' to be inserted)
                                and pos (at which position the letter needs to be inserted)
                            -> This function basically insert the letter at a given position on the board

spaceIsFree(pos0) -----------> This fucntion takes only one argument i.e. pos
                            -> It returns trur if position pos is empty on board, else return false

printBoard(board) -----------> This function takes only one argument board (a list)
                            -> It prints the board on the console (means how the board looks after particular move)

isBoardFull(board) ----------> This function also takes only one argument board.
                            -> It return true if none of the space is empty on board, else return true


IsWinner(board,letter) ------> This function takes two arguments, first board and second letter
                            -> It basically checks if for given letter, is there any 3 continous letter among any of the 8 possible case
                                if there is then return s true, else return fasle

playerMove() ----------------> this function basically ask player to input the position where he/she wants to add his/her letter.
                            -> This function first checks all the possibel validation required for inerting letter at inputed pos,
                                 like, is pos in board is empty, pos must be an integer [1,9]
                            -> if validity is satisfied, it basically add players letter at inputed pos.

computerMove() --------------> this function is defined for making the computer take its move
                            -> In thsi funtion, first it checks all the position where computer can insert letter,
                                 then consider all possible case and checks which is optimal
                            -> It also checks, all the corners, center, and edge cases also


selectRandom(li) ------------> This function takes one argument that is list, and returns any random value from the list
                            -> we have used this function in the computermove() function

Then at last main function is defined, which basically makes calls to each function and starts the game.

'''


# list board created to store which letter is assigned at particlar position,
# we have taken size till 10, because in board 0 is not included in board
board = [' ' for x in range(10)]


# funtion designed to take the input from the player,(the position ofy the box) ----------------------------------
def insertLetter(letter, pos):
    if isBoardFull(board): # if the board is full, them we return the message that, "None of you won!"
        return "None of you won!"
    else:
        board[pos] = letter


# funciton to check if there is free space at position pos, to enter the value ----------------------------------
def spaceIsFree(pos):
    return board[pos] == ' '


# function defined for printing the look of board after each move --------------------------------------------
def printBoard(board):
    # print('-------------------------')
    print('       |       |       ')
    print('   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3] + '   ')
    print('       |       |       ')
    print('-------------------------')
    print('       |       |       ')
    print('   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6] + '   ')
    print('       |       |       ')
    print('-------------------------')
    print('       |       |       ')
    print('   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9] + '   ')
    print('       |       |       ')
    # print('-------------------------')


# function to check if board is full, or not -----------------------------------------------------------
def isBoardFull(board):
    if board.count(' ') > 1: # for checking we just count the empty string , then there is some space present
        return False
    else:
        return True


# function defined to check who is the winner, wither player or computer -----------------------------------------
def IsWinner(board,letter): # here we check all the cases
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))


# function defined for player move ----------------------------------------------------------------------
def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9 : ") # taken input from player
        try:
            move = int(move) # type casting the imput into integer
            if move > 0 and move < 10:
                if spaceIsFree(move): # if input is valid, then add input at that positoon
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied.')
            else:
                print('Please type a number between 1 and 9.')

        except:
            print('Please type a number.') # when try code is not run, then this message will be displayed


# function defined for computer move ----------------------------------------------------------------------
def computerMove():
    # first we get list of positon where computer can entered it's letter
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O', 'X']: # we just loop through all possible values and checks for the correct/optimal position for computer
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    # checking all the corner values
    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]: # 4 corners are at position 1,3,7,9, sowe check for all position
            cornersOpen.append(i)
    if len(cornersOpen) > 0: # if conditon satisfied, we take any random position from corner position we got
        move = selectRandom(cornersOpen)
        return move

    # checking for center position that is 5
    if 5 in possibleMoves:
        move = 5
        return move

    # checking ofr edge postion , that are 2,4,6,8
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:# if conditon satisfied, we take any random position from edge position we got
        move = selectRandom(edgesOpen)
        return move


# function defined to select random position for the list that is passed as parameter --------------------------
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


# function defined for the main logic of the game -----------------------------------------------------------------
def main():
    print("Welcome to the game!") # printing the starting message
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board) # printing the updated board
        else:
            print("Sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an O on position ' , move , ':')
                printBoard(board) # printing the updated board
        else:
            print("You won!")
            break

    if isBoardFull(board): # is board is full, so we tie the game, as no one won and board become full
        print("The game tied.")


# running the while loop for playing game till player wants -------------
while True:
    x = input("Do you want to play again? (y/n) : ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------')
        main()
    else: # if player entered n, just break through loop
        break
