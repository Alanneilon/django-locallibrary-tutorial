def showBoard(board):
    print(board)
#####################################################################################################
def playerMove():
    move=''
    while move=='':
        try:
            move=int(input("Please enter a number between 1 and 9 :"))
        except:
            print ("Incorrect ")
            continue
        return move
############################################################################################################
def playerChoice(player):
    while True:
        playerChoice=playerMove()
        if 0<playerChoice<10:
            enterChoiceOnBoard(playerChoice, player)
            print("Move Accepted ")
            break
        print ("Invalid number range entered: ")
    return playerChoice
##########################################################################################################
def enterChoiceOnBoard(choice, player):
    if board[choice-1]=='X' or board[choice-1]=='O':
        print("This position is taken ")
        playerChoice(player)
    if player=='Player 1':
        board[choice-1]='X'
    else:
        board[choice-1]='O'
###############################################################################################################
def playGame():
    count=0
    player=''
    while count<9:
        if count%2==1:
            player="Player 1"
        else:
            player="Player 2"
        showBoard(board)
        playerChoice(player)
        showBoard(board)
        if checkWinner(board)==True:
            break
        else:
            print("Your Turn")
        print(player)
        count+=1
###############################################################################################################
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



board=[0,1,2,3,4,5,6,7,8]
playGame()


#showBoard(board)

#playerChoice()

#showBoard(board)




