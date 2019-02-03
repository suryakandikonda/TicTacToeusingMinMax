from tkinter import *
import tkinter.messagebox

tk = Tk()

tk.title("Tic Tac Toe")



player = 'x'
opponent = 'o'
tic = [['_','_','_'],['_','_','_'],['_','_','_']]
bestVal = 0
score = 0

def starting():
    lab = Label(text="Designed and Developed by Surya Kandikonda",font=('Verdana',12))
    startGame = Button(tk, text="Start Game", bg="#42d7f4", font=('Times 10 bold italic'), height = 4, width = 20, command = lambda:tknewGame())
    startGame.grid(row=1,column = 2)


def tknewGame():
    buttons = StringVar()
    global button1,button2,button3,button4,button5,button6,button7,button8,button9

    button1 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button1a())
    button1.grid(row=0, column = 0, sticky = S+N+E+W)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button2a())
    button2.grid(row=0, column = 1, sticky = S+N+E+W)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button3a())
    button3.grid(row=0, column = 2, sticky = S+N+E+W)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button4a())
    button4.grid(row=1, column = 0, sticky = S+N+E+W)

    button5 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button5a())
    button5.grid(row=1, column = 1, sticky = S+N+E+W)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button6a())
    button6.grid(row=1, column = 2, sticky = S+N+E+W)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button7a())
    button7.grid(row=2, column = 0, sticky = S+N+E+W)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button8a())
    button8.grid(row=2, column = 1, sticky = S+N+E+W)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height = 4, width = 8, command = lambda:button9a())
    button9.grid(row=2, column = 2, sticky = S+N+E+W)

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
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
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
    if(bestMoverow==0 and bestMovecol == 0):
        button1["text"]="X"
    if(bestMoverow==0 and bestMovecol == 1):
        button2["text"]="X"
    if(bestMoverow==0 and bestMovecol == 2):
        button3["text"]="X"
    if(bestMoverow==1 and bestMovecol == 0):
        button4["text"]="X"
    if(bestMoverow==1 and bestMovecol == 1):
        button5["text"]="X"
    if(bestMoverow==1 and bestMovecol == 2):
        button6["text"]="X"
    if(bestMoverow==2 and bestMovecol == 0):
        button7["text"]="X"
    if(bestMoverow==2 and bestMovecol == 1):
        button8["text"]="X"
    if(bestMoverow==2 and bestMovecol == 2):
        button9["text"]="X"

        
    if(evaluate(board)==10):
        tkinter.messagebox.showinfo("Winner X", "Computer won the game")
        flush()
        starting()
    if(evaluate(board)==-10):
        tkinter.messagebox.showinfo("Winner O", "You won the game")
        flush()
        starting()
    elif(isMovesLeft(board)==False):
        tkinter.messagebox.showinfo("Game Over", "TIE!!")
        flush()
        tknewGame()
        starting()
    

def flush():
    global tic,bestVal,score
    tic = [['_','_','_'],['_','_','_'],['_','_','_']]
    bestVal = 0
    score = 0
    



def button1a():
    global tic,player,opponent,button1
    if(button1["text"]=="X" or button1["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        button1["text"]="O"
        tic[0][0]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button2a():
    global tic,player,opponent,button2
    if(button2["text"]=="X" or button2["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")

    else:
        
        button2["text"]="O"
        
        tic[0][1]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button3a():
    global tic,player,opponent,button3
    if(button3["text"]=="X" or button3["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")

    else:    
        button3["text"]="O"
        
        tic[0][2]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button4a():
    global tic,player,opponent,button4
    if(button4["text"]=="X" or button4["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        
        button4["text"]="O"
        
        tic[1][0]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button5a():
    global tic,player,opponent,button5
    if(button5["text"]=="X" or button5["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        button5["text"]="O"
        
        tic[1][1]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button6a():
    global tic,player,opponent,button6
    if(button6["text"]=="X" or button6["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        button6["text"]="O"
        
        tic[1][2]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button7a():
    global tic,player,opponent,button7
    if(button7["text"]=="X" or button7["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        
        button7["text"]="O"
        
        tic[2][0]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button8a():
    global tic,player,opponent,button8
    if(button8["text"]=="X" or button8["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        button8["text"]="O"
        
        tic[2][1]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)

def button9a():
    global tic,player,opponent,button9
    if(button9["text"]=="X" or button9["text"]=="O"):
        tkinter.messagebox.showinfo("Oops!","Position already taken")
    else:
        button9["text"]="O"
        
        tic[2][2]=opponent
        if(isMovesLeft(tic)==False):
            tkinter.messagebox.showinfo("Game Over!!","TIE!!!")
            flush()
            tknewGame()
            starting()
        else:
            findBestMove(tic)


    



if __name__=='__main__':
    starting()

tk.mainloop()
    
    


    
