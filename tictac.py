#Function to print the list in a board formation
def showBoard(board):
    print("1.|" +board[0]+ "| 2.|" +board[1]+ "| 3.|" +board[2]+ "| ")
    print("4.|" +board[3]+ "| 5.|" +board[4]+ "| 6.|" +board[5]+ "| ")
    print("7.|" +board[6]+ "| 8.|" +board[7]+ "| 9.|" +board[8]+ "| ")
#####################################################################################################
#Function to take the players choice as a number
def playerMove():
    move=''
    #Loop to continually ask the user for input until a number is entered. If a number is not entered an 
    # expception is thrown
    while move=='':
        try:
            move=int(input("Please enter a number between 1 and 9 :"))
        except:
            print ("Incorrect ")
            continue
        return move
############################################################################################################
#This function will take the players chosen number and ensure that it is within the correct number range
def playerChoice(player):
#if the number entered is in the correct range, enter it onto the board list, if not dont enter
# the number and let the user know 
    while True:
        playerChoice=playerMove()
        if 0<playerChoice<10:
            enterChoiceOnBoard(playerChoice, player)
            print("Move Accepted ")
            break
        print ("Invalid number range entered: ")
    return playerChoice
##########################################################################################################
#Function to take the accepted user entry and enter it on the board list provided the position is not already
#taken. Depending on the player number, if its player 1 enter an X in the chosen postion. If player 2, enter an O
def enterChoiceOnBoard(choice, player):
    if board[choice-1]=='X' or board[choice-1]=='O':
        print("This position is taken ")
        playerChoice(player)
    if player=='Player 1':
        board[choice-1]='X'
    else:
        board[choice-1]='O'
###############################################################################################################
#This is the main driving function of the program. It will decide the when and where all the other functions are 
#called. As there are 9 positions on the board, I set the while loop to go around at most 9 times. I use this count
#to calculate which players turn it is
def playGame():
    count=0
    player=''
    while count<9:
        if count%2==1:
            player="Player 2"
        else:
            player="Player 1"
        #The board is shown to the players
        showBoard(board)
        #ask the player for their choice. If their choice is of the required quality enter it on the board then
        #show the board
        playerChoice(player)
        showBoard(board)
        #Check to see if there is a winner. If there is break out of the loop to end the program
        #if now winner is found the loop continues
        if checkWinner(board)==True:
            break
        else:
            print("Thank you ")
            print(player)
            print("Next Player please ")
        count+=1
        
###############################################################################################################
#Function to check if there is a winner. This will be a boolean function which will return true for false.
#Initialise the winner flag to false, then check all possible winning combinations on the board while winner is
#false. When a winnder is found set the flag to true, break for the loop and return true to the function caller
def checkWinner(board):
    winner=False
    while winner==False:
        if board[0]=='X' and board[1]=='X' and board[2]=='X':
            print("Well done, player1. You won")
            winner=True
            break
        elif board[0]=='O' and board[1]=='O' and board[2]=='O':
            print("Well done, player 2. You won!")
            winner=True
            break
        elif board[3]=='X' and board[4]=='X' and board[5]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[3]=='O' and board[4]=='O' and board[5]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[6]=='X' and board[7]=='X' and board[8]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[6]=='O' and board[7]=='O' and board[8]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[0]=='X' and board[3]=='X' and board[6]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[0]=='O' and board[3]=='O' and board[6]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[1]=='X' and board[4]=='X' and board[7]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[1]=='O' and board[4]=='O' and board[7]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[2]=='X' and board[5]=='X' and board[8]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[2]=='O' and board[5]=='O' and board[8]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[0]=='X' and board[4]=='X' and board[8]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[0]=='O' and board[4]=='O' and board[8]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        elif board[2]=='X' and board[4]=='X' and board[6]=='X':
            print("Well done, player 1. You won")
            winner=True
            break
        elif board[2]=='O' and board[4]=='O' and board[6]=='O':
            print("Well done, player 2. You won")
            winner=True
            break
        else:
            break

    return winner

###############################################################################################################
#main program. Initialise the board values as blank strings then call the main function to play the game

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
playGame()






