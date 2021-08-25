import copy
import alphaBetaPruning
from heuristics import*
import random

VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board

rows=6
columns=7


class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    
     #Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
    
        return [s.board, 0.00001, s.playTurn, rows*columns]     # 0 is TIE

def cpy(s1):
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        #print("board ", s2.board)
        return s2
    
    
    
def value(s):
    if winningCase(s):
        return VICTORY

    if losingCase(s):
        return LOSS

    if compThreeCase(s):
        return 500

    return random.random()*10
        

def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        for r in range(rows):
            print("\n|",end="")
        #print("\n",len(s[0][0])*" --","\n|",sep="", end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")

        print()

        for i in range(columns):
            print(" ",i,sep="",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")



def isFinished(s):
#Seturns True iff the game ended
        if s.size==0:
            return True
        
        # Check Rows for final state
        for i in range(rows):
            countHuman=0
            countComp=0
            for j in range(columns):
                if s.board[i][j]==HUMAN:
                    countComp=0
                    countHuman+=1
                if s.board[i][j]==COMPUTER:
                    countHuman=0
                    countComp+=1
                if s.board[i][j]==0:
                    countHuman=0
                    countComp=0
                if countComp==4 or countHuman==4:
                    return True

        # Check Columns for final state
        for j in range(columns):
            countHuman=0
            countComp=0
            for i in range(rows):
                if s.board[i][j]==HUMAN:
                    countComp=0
                    countHuman+=1
                if s.board[i][j]==COMPUTER:
                    countHuman=0
                    countComp+=1
                if s.board[i][j]==0:
                    countHuman=0
                    countComp=0
                if countComp==4 or countHuman==4:
                    return True

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            countHuman=0
            countComp=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countComp=0
                    countHuman+=1
                if s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countHuman=0
                    countComp+=1
                if s.board[min(rows, line) - j - 1][start_col + j]==0:
                    countHuman=0
                    countComp=0
                if countComp==4 or countHuman==4:
                    return True

        # Check Downward Diagonal for final state
        ans = [[] for i in range(rows + columns - 1)]
        for i in range(rows):
            for j in range(columns):
                ans[i - j + 3].append(s.board[i][j])

        for i in range(len(ans)):
            countHuman=0
            countComp=0
            for j in range(len(ans[i])):
                if ans[i][j]==HUMAN:
                    countComp=0
                    countHuman+=1
                if ans[i][j]==COMPUTER:
                    countHuman=0
                    countComp+=1
                if ans[i][j]==0:
                    countHuman=0
                    countComp=0
                if countComp==4 or countHuman==4:
                    return True
        return False


def isHumTurn(s):
#Returns True iff it is the human's turn to play
        return s.playTurn==HUMAN
    


def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-me / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN
            
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for huma. or comp.) in col. c
#and switches turns.
#Assumes the move is legal.

        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER

   
def inputMove(s):
#Reads, enforces legality and executes the user's move.

        #self.printState()
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")

            else:
                flag=False
                makeMove(s,c)

        
def getNext(s):
#returns a list of the next states of s
        ns=[]
        for c in list(range(columns)):
            #print("c=",c)
            if s.board[0][c]==0:
                #print("possible move ", c)
                tmp=cpy(s)
                makeMove(tmp, c)
                #print("tmp board=",tmp.board)
                ns+=[tmp]
                #print("ns=",ns)
        #print("returns ns ", ns)
        return ns

def inputComputer(s):    
        return alphaBetaPruning.go(s)


#==========================================================================================
#===================================   Heuristics  ========================================
#==========================================================================================


def winningCase(s):
    # Check Rows for final state
        for i in range(rows):
            countComp=0
            for j in range(columns):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                if countComp==4:
                    return True

        # Check Columns for final state
        for j in range(columns):
            countComp=0
            for i in range(rows):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                if countComp==4:
                    return True

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            countComp=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countComp+=1
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countComp=0
                if countComp==4:
                    return True

        # Check Downward Diagonal for final state
        ans = [[] for i in range(rows + columns - 1)]
        for i in range(rows):
            for j in range(columns):
                ans[i - j + 3].append(s.board[i][j])

        for i in range(len(ans)):
            countComp=0
            for j in range(len(ans[i])):
                if ans[i][j]==COMPUTER:
                    countComp+=1
                if ans[i][j]==0 or ans[i][j]==HUMAN:
                    countComp=0
                if countComp==4:
                    return True
        
        return False

def losingCase(s):
    # Check Rows for final state
        for i in range(rows):
            countHuman=0
            for j in range(columns):
                if s.board[i][j]==HUMAN:
                    countHuman+=1
                if s.board[i][j]==0 or s.board[i][j]==COMPUTER:
                    countHuman=0
                if countHuman==4:
                    return True

        # Check Columns for final state
        for j in range(columns):
            countHuman=0
            for i in range(rows):
                if s.board[i][j]==HUMAN:
                    countHuman+=1
                if s.board[i][j]==0 or s.board[i][j]==COMPUTER:
                    countHuman=0
                if countHuman==4:
                    return True

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            countHuman=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countHuman+=1
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countHuman=0
                if countHuman==4:
                    return True

        # Check Downward Diagonal for final state
        ans = [[] for i in range(rows + columns - 1)]
        for i in range(rows):
            for j in range(columns):
                ans[i - j + 3].append(s.board[i][j])

        for i in range(len(ans)):
            countHuman=0
            for j in range(len(ans[i])):
                if ans[i][j]==HUMAN:
                    countHuman+=1
                if ans[i][j]==0 or ans[i][j]==COMPUTER:
                    countHuman=0
                if countHuman==4:
                    return True
        return False

def compThreeCase(s):
    # Check Rows for final state
        for i in range(rows):
            emptySlot = False
            countComp=0
            for j in range(columns):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                    #check that there's an empty slot to make it four
                    if j!=0 and s.board[i][j-1]==0:
                        emptySlot=True
                    if j!=(columns-1) and s.board[i][j+1]==0:
                        emptySlot=True
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                    emptySlot=False
                if countComp==3 and emptySlot:
                    return True

        # Check Columns for final state
        for j in range(columns):
            countComp=0
            for i in range(rows):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                if countComp==3:
                    return True

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            countComp=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countComp+=1
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countComp=0
                if countComp==3:
                    return True

        # Check Downward Diagonal for final state
        ans = [[] for i in range(rows + columns - 1)]
        for i in range(rows):
            for j in range(columns):
                ans[i - j + 3].append(s.board[i][j])

        for i in range(len(ans)):
            countComp=0
            for j in range(len(ans[i])):
                if ans[i][j]==COMPUTER:
                    countComp+=1
                if ans[i][j]==0 or ans[i][j]==HUMAN:
                    countComp=0
                if countComp==3:
                    return True
        
        return False