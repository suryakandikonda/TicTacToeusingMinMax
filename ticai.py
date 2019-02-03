player = 'x'
opponent = 'o'
tic = [['_','_','_'],['_','_','_'],['_','_','_']]
bestVal = 0
score = 0

def isMovesLeft(board):
    i=0
    j=0
    while(i<len(board)):
        j=0
        while(j<len(board)):
            if(board[i][j]=='_'):
                return True
            j+=1
        i+=1
    return False

def evaluate(b):
    i=0
    j=0
    global player,opponent
    while(i<len(b)):
        if(b[i][0]==b[i][1] and b[i][1]==b[i][2]):
            if(b[i][0]==player):
                return +10
            elif(b[i][0]==opponent):
                return -10
        i+=1

    while(j<len(b)):
        if(b[0][j]==b[1][j] and b[1][j]==b[2][j]):
            if(b[0][j]==player):
                return +10
            elif(b[0][j]==opponent):
                return -10
        j+=1

    if(b[0][0]==b[1][1] and b[1][1]==b[2][2]):
        if(b[0][0]==player):
            return +10
        elif(b[0][0]==opponent):
            return -10

    if(b[0][2]==b[1][1] and b[1][1]==b[2][0]):
        if(b[0][2]==player):
            return +10
        elif(b[0][2]==opponent):
            return -10

    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    global player,opponent

    if(score==+10):
        return score

    if(score==-10):
        return score

    if(isMovesLeft(board)==False):
        return 0

    if(isMax):
        best = -1000

        i=0
        j=0
        while(i<len(board)):
            j=0
            while(j<len(board)):
                if(board[i][j]=='_'):
                    board[i][j]=player
                    best = max(best,minimax(board,depth+1,not isMax))
                    board[i][j]='_'
                j+=1
            i+=1
        return best
    else:
        best = 1000
        i=0
        j=0
        while(i<len(board)):
            j=0
            while(j<len(board)):
                if(board[i][j]=='_'):
                    board[i][j]=opponent
                    best = min(best,minimax(board,depth+1,not isMax))
                    board[i][j]='_'
                j+=1
            i+=1
        return best

def findBestMove(board):
    global player,opponent,bestVal,score
    bestVal=-1000
    bestMoverow=-1
    bestMovecol = -1
    i=0
    j=0
    while(i<len(board)):
        j=0
        while(j<len(board)):
            if(board[i][j]=='_'):
                board[i][j]=player
                moveVal = minimax(board,0,False)
                board[i][j]='_'

                if(moveVal > bestVal):
                    bestMoverow = i
                    bestMovecol = j
                    bestVal = moveVal
            j+=1
        i+=1

    board[bestMoverow][bestMovecol]=player
    print("Computer Placed!!")
    printBoard()
    if(evaluate(board)==10):
        print("Computer Won!!")
        flush()
    if(evaluate(board)==-10):
        print("Player Won!!")
        flush()
    elif(isMovesLeft(board)==False):
        print("Game Over!!")
        flush()
    newGame()

def flush():
    global tic,bestVal,score
    tic = [['_','_','_'],['_','_','_'],['_','_','_']]
    bestVal = 0
    score = 0
    print("")
    print("")
    print("------NEW GAME------")
    print("")
    print("")
    newGame()
    

def newGame():
    global tic,player,opponent
    r = int(input("Enter row value"))
    c = int(input("Enter col value"))
    if(tic[r][c]==player or tic[r][c]==opponent):
        print("Already Placed")
        newGame()
    else:
        tic[r][c]=opponent
        if(isMovesLeft(tic)==False):
            printBoard()
            flush()
        else:
            printBoard()
            findBestMove(tic)

def printBoard():
    global tic
    i=0
    j=0
    while(i<len(tic)):
        j=0
        while(j<len(tic)):
            print(" ",tic[i][j]," ",end="")
            j+=1
        print("")
        i+=1
    



if __name__=='__main__':
    newGame()
    
    


    
