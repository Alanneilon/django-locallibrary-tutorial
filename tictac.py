def showBoard(board):
    print(board)

def playerMove():
    move=''
    while move=='':
        try:
            move=int(input("Please enter a number between 1 and 9 :"))
        except:
            print ("Incorrect ")
            continue
        return move

def playerChoice():
    valid=False
    
    while valid==False:
        playerChoice=playerMove()
        if playerChoice<1 | playerChoice>9:
            print("Invalid number range ")
            playerMove()
        else:
            print ("Move accepted ")
            valid=True
            break

    return playerChoice


board=[0,1,2,3,4,5,6,7,8]

showBoard(board)

playerChoice()




