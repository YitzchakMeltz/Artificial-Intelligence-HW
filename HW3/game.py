import copy
import alphaBetaPruning
import random
import time

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

    totalBoardValue=0

    if compThreeCaseTrap(s):
        totalBoardValue += 10**7

    if humanDoubleTrapping(s):
        totalBoardValue -= 10**6

    totalBoardValue += compThreeCase(s)

    totalBoardValue += humanThreeCase(s)

    totalBoardValue += doubleThreat(s,'C')

    totalBoardValue += doubleThreat(s,'H')

    return totalBoardValue + mapSmallestToLargest(boardValue(s))
        

def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        print("Value",value(s))
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
            return COMPUTER
        elif val==LOSS:
            print("You beat me!")
            return HUMAN
        elif val==TIE:
            print("It's a TIE")
        return TIE



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

   
def inputMove(s,col):
#Reads, enforces legality and executes the user's move.

        #self.printState()
        flag=True
        while flag:
            #c=int(input("Enter your next move: "))
            c=col
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
        #total sum of board value
        totalSum=0

        # Check Rows for final state
        for i in range(rows):
            emptySlot = False
            left=0
            right=0
            countComp=0
            for j in range(columns):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                    #check that there's an empty slot to make it four
                    if j!=0 and s.board[i][j-1]==0:
                        emptySlot=True
                        lower=i-1
                        while lower>0 and s.board[lower][j-1]==0:
                            left+=1
                            lower-=1
                    if j!=(columns-1) and s.board[i][j+1]==0:
                        emptySlot=True
                        lower=i-1
                        while lower>0 and s.board[lower][j+1]==0:
                            right+=1
                            lower-=1
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                    emptySlot=False
                    right=0
                    left=0
                if countComp==3 and emptySlot:
                    if right==0 and left==0:
                        return 500
                    totalSum += 500 + 2*mapSmallestToLargest(right) + 2*mapSmallestToLargest(left)

        # Check Columns for final state
        for j in range(columns):
            emptySlot = False
            countComp=0
            for i in range(rows):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                    #check that there's an empty slot to make it four
                    if i!=0 and s.board[i-1][j]==0:
                        emptySlot=True
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                    emptySlot=False
                if countComp==3 and emptySlot:
                    totalSum += 500

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            emptySlot = False
            countComp=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countComp+=1
                     #check that there's an empty slot to make it four
                    if (min(rows, line) - j < i) and (start_col + j < j - 1) and s.board[min(rows, line) - j][start_col + j + 1]==0:
                        emptySlot=True
                    if (min(rows, line) - j - 1> 0) and (start_col + j > 0) and s.board[min(rows, line) - j - 2][start_col + j - 1]==0:
                        emptySlot=True
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countComp=0
                    emptySlot=False
                if countComp==3 and emptySlot:
                    totalSum += 500

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
                    totalSum += 500
        
        return totalSum

def humanThreeCase(s):
        #total sum of board value
        totalSum=0

        # Check Rows for final state
        for i in range(rows):
            emptySlot = False
            left=0
            right=0
            countHuman=0
            for j in range(columns):
                if s.board[i][j]==HUMAN:
                    countHuman+=1
                    #check that there's an empty slot to make it four
                    if j!=0 and s.board[i][j-1]==0:
                        emptySlot=True
                        lower=i-1
                        while lower>0 and s.board[lower][j-1]==0:
                            left-=1
                            lower-=1
                    if j!=(columns-1) and s.board[i][j+1]==0:
                        emptySlot=True
                        lower=i-1
                        while lower>0 and s.board[lower][j+1]==0:
                            right-=1
                            lower-=1
                if s.board[i][j]==0 or s.board[i][j]==COMPUTER:
                    countHuman=0
                    right=0
                    lower=0
                    emptySlot=False
                if countHuman==3 and emptySlot:
                    if right==0 and left==0:
                        return -500
                    totalSum -= (500 + 2*mapSmallestToLargest(right) + 2*mapSmallestToLargest(left))

        # Check Columns for final state
        for j in range(columns):
            emptySlot = False
            countHuman=0
            for i in range(rows):
                if s.board[i][j]==HUMAN:
                    countHuman+=1
                    #check that there's an empty slot to make it four
                    if i!=0 and s.board[i-1][j]==0:
                        emptySlot=True
                if s.board[i][j]==0 or s.board[i][j]==COMPUTER:
                    countHuman=0
                    emptySlot=False
                if countHuman==3 and emptySlot:
                    totalSum -= 500

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            emptySlot = False
            countHuman=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countHuman+=1
                     #check that there's an empty slot to make it four
                    if (min(rows, line) - j < i) and (start_col + j < j - 1) and s.board[min(rows, line) - j][start_col + j + 1]==0:
                        emptySlot=True
                    if (min(rows, line) - j - 1> 0) and (start_col + j > 0) and s.board[min(rows, line) - j - 2][start_col + j - 1]==0:
                        emptySlot=True
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countHuman=0
                    emptySlot=False
                if countHuman==3 and emptySlot:
                    totalSum -= 500

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
                if countHuman==3:
                    totalSum -= 500
        
        return totalSum

def compThreeCaseTrap(s):
        # Check Rows for final state
        for i in range(rows):
            emptySlot = False
            fillableLeft= False
            fillableRight = False
            countComp=0
            for j in range(columns):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                    #check that there's an empty slot to make it four
                    if j!=0 and s.board[i][j-1]==0 and (i==rows-1 or s.board[i+1][j-1]!=0):
                        emptySlot=True
                        fillableLeft=True
                    if j!=(columns-1) and s.board[i][j+1]==0 and (i==rows-1 or s.board[i+1][j+1]!=0):
                        emptySlot=True
                        fillableRight=True
                if s.board[i][j]==0 or s.board[i][j]==HUMAN:
                    countComp=0
                    emptySlot=False
                    fillableRight=False
                    fillableLeft=False
                if countComp==3 and emptySlot and fillableLeft and fillableRight:
                    return True

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            emptySlot = False
            countComp=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==COMPUTER:
                    countComp+=1
                     #check that there's an empty slot to make it four
                    if (min(rows, line) - j < i) and (start_col + j < j - 1) and s.board[min(rows, line) - j][start_col + j + 1]==0:
                        emptySlot=True
                    if (min(rows, line) - j - 1> 0) and (start_col + j > 0) and s.board[min(rows, line) - j - 2][start_col + j - 1]==0:
                        emptySlot=True
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==HUMAN:
                    countComp=0
                    emptySlot=False
                if countComp==3 and emptySlot:
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

def humanDoubleTrapping(s):
    # Check Rows for final state
        for i in range(rows):
            emptySlot = False
            fillableLeft= False
            fillableRight = False
            countHuman=0
            for j in range(columns):
                if s.board[i][j]==HUMAN:
                    countHuman+=1
                    #check that there's an empty slot to make it three double trap
                    if j!=0 and s.board[i][j-1]==0 and (i==rows-1 or s.board[i+1][j-1]!=0):
                        emptySlot=True
                        fillableLeft=True
                    if j!=(columns-1) and s.board[i][j+1]==0 and (i==rows-1 or s.board[i+1][j+1]!=0):
                        emptySlot=True
                        fillableRight=True
                if s.board[i][j]==0 or s.board[i][j]==COMPUTER:
                    countHuman=0
                    emptySlot=False
                    fillableLeft=False
                    fillableRight=False
                if countHuman==2 and emptySlot and fillableLeft and fillableRight:
                    return True

        return False

def doubleThreat(s,player):
    THREAT = 10
    FILLED = 20
    EMPTY = 30
    
    sumValue=0

    threatBoard = createThreatBoard(s,player)

    for j in range(columns-1,0,-1):
        countHeight = 0
        countThreats = 0
        for i in range(rows-1,0,-1):
            if threatBoard[i][j] == THREAT:
                countThreats += 1
            if threatBoard[i][j] == EMPTY or threatBoard[i][j] == FILLED:
                countThreats = 0
            if countThreats == 2:
                for k in range(i+1,0,-1):
                    if threatBoard[k][j] == EMPTY:
                        countHeight += 1
                if player == 'C':
                    sumValue += 6000 + 2*mapSmallestToLargest(countHeight)
                if player == 'H':
                    sumValue -= 6000 + 2*mapSmallestToLargest(countHeight)

    return sumValue


def boardValue(s):
    sumOfValues=0
    for i in range(rows):
        for j in range(columns):
            if s.board[i][j]==5:
                sumOfValues += abs(j - (columns//2)) + abs(i-rows-1)

    return sumOfValues

def mapSmallestToLargest(num):
    if num !=0:
        return (1/num) * 110
    return 1

def createThreatBoard(s,player):
    if player == 'C':
        OUR_SIDE=COMPUTER
        AGAINST=HUMAN
    else:
        OUR_SIDE=HUMAN
        AGAINST=COMPUTER

    #create threat board
    threatBoard=[]
    for i in range(rows):
            threatBoard = threatBoard+[columns*[0]]

    THREAT = 10
    FILLED = 20
    EMPTY = 30

    for i in range(rows):  
        for j in range(columns):
            threatBoard[i][j]=EMPTY

    #fill threat board
    # Check Rows for final state
        for i in range(rows):
            emptySlotRight = False
            emptySlotLeft = False
            countHuman=0
            for j in range(columns):
                if s.board[i][j]==OUR_SIDE:
                    countHuman+=1
                    #check that there's an empty slot to make it four
                    if j!=0 and s.board[i][j-1]==0:
                        emptySlotLeft=True
                    if j!=(columns-1) and s.board[i][j+1]==0:
                        emptySlotRight=True
                if s.board[i][j]==0 or s.board[i][j]==AGAINST:
                    countHuman=0
                    emptySlotRight=False
                    emptySlotLeft-False
                if countHuman==3 and emptySlotLeft:
                    threatBoard[i][j-1]=THREAT
                    if i>0:
                        lower=i-1
                        while lower>0:
                            if s.board[lower][j-1]==COMPUTER or s.board[lower][j-1]==HUMAN:
                                threatBoard[lower][j-1] = FILLED
                            lower -= 1
                if countHuman==3 and emptySlotRight:
                    threatBoard[i][j+1]=THREAT
                    if i>0:
                        lower=i-1
                        while lower>0:
                            if s.board[lower][j+1]==COMPUTER or s.board[lower][j+1]==HUMAN:
                                threatBoard[lower][j+1] = FILLED
                            lower -= 1
                    
        # Check Columns for final state
        for j in range(columns):
            emptySlot = False
            countHuman=0
            for i in range(rows):
                if s.board[i][j]==OUR_SIDE:
                    countHuman+=1
                    #check that there's an empty slot to make it four
                    if i!=0 and s.board[i-1][j]==0:
                        emptySlot=True
                if s.board[i][j]==0 or s.board[i][j]==AGAINST:
                    countHuman=0
                    emptySlot=False
                if countHuman==3 and emptySlot:
                    threatBoard[i-1][j]=THREAT
                    if i!=(rows-1):
                        lower = i-1
                        while lower<rows:
                            threatBoard[lower][j]=FILLED
                            lower += 1

        # Check Upward Diagonal for final state
        for line in range(1, (rows + columns)):
            emptySlotRight = False
            emptySlotLeft = False
            countHuman=0
            start_col = max(0, line - rows)
            count = min(line, (columns - start_col), rows)
            for j in range(0, count):
                if s.board[min(rows, line) - j - 1][start_col + j]==OUR_SIDE:
                    countHuman+=1
                     #check that there's an empty slot to make it four
                    if (min(rows, line) - j < i) and (start_col + j < j - 1) and s.board[min(rows, line) - j][start_col + j + 1]==0:
                        emptySlotLeft=True
                    if (min(rows, line) - j - 1> 0) and (start_col + j > 0) and s.board[min(rows, line) - j - 2][start_col + j - 1]==0:
                        emptySlotRight=True
                if s.board[min(rows, line) - j - 1][start_col + j]==0 or s.board[min(rows, line) - j - 1][start_col + j]==AGAINST:
                    countHuman=0
                    emptySlotRight=False
                    emptySlotLeft=False
                if countHuman==3 and emptySlotLeft:
                    lower = 1
                    while min(rows, line) - j - lower >=0:
                        if s.board[min(rows, line) - j - lower][start_col + j + 1]==COMPUTER or s.board[min(rows, line) - j - lower][start_col + j + 1]==HUMAN:
                            threatBoard[min(rows, line) - j - lower][start_col + j + 1] = FILLED
                        lower -= 1
                if countHuman==3 and emptySlotRight:
                    lower = 1
                    while (min(rows, line) - j - 2 - lower) > rows:
                        if s.board[min(rows, line) - j - 2 - lower][start_col + j - 1]==COMPUTER or s.board[min(rows, line) - j - 2 - lower][start_col + j - 1]==HUMAN:
                            threatBoard[min(rows, line) - j - 2 - lower][start_col + j - 1] = FILLED
                        lower -= 1
    return threatBoard

    #====================================================================
    #=============================== GUI ================================
