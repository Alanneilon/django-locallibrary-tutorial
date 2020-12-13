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
    
    while True:
        playerChoice=playerMove()
        if 0<playerChoice<10:
            print("Move Accepted")
            break
        print ("Invalid number range entered: ")
    return playerChoice


board=[0,1,2,3,4,5,6,7,8]

showBoard(board)

playerChoice()




