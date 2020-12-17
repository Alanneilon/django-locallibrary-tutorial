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
        playerChoice(player)
        showBoard(board)
        print("Your Turn")
        print(player)
        count+=1
###############################################################################################################
board=[0,1,'X',3,'O',5,6,7,8]
playGame()


#showBoard(board)

#playerChoice()

#showBoard(board)




