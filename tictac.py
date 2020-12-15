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
def playerChoice():
    while True:
        playerChoice=playerMove()
        if 0<playerChoice<10:
            enterChoiceOnBoard(playerChoice)
            print("Move Accepted ")
            break
        print ("Invalid number range entered: ")
    return playerChoice
##########################################################################################################
def enterChoiceOnBoard(choice):
    if board[choice-1]=='X' or board[choice-1]=='O':
        print("This position is taken ")
        playerChoice()
    else:
        board[choice-1]='X'
###############################################################################################################
def playGame():
    count=0
    while count<9:
        playerChoice()
        showBoard(board)
        count+=1
###############################################################################################################
board=[0,1,'X',3,'O',5,6,7,8]
playGame()


#showBoard(board)

#playerChoice()

#showBoard(board)




