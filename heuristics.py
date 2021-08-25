import game

def winningCase(s):
    # Check Rows for final state
        for i in range(rows):
            countComp=0
            for j in range(columns):
                if s.board[i][j]==COMPUTER:
                    countHuman=0
                    countComp+=1
                if s.board[i][j]==0:
                    countComp=0
                if countComp==4:
                    return True

        # Check Columns for final state
        for j in range(columns):
            countComp=0
            for i in range(rows):
                if s.board[i][j]==COMPUTER:
                    countComp+=1
                if s.board[i][j]==0:
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
                if s.board[min(rows, line) - j - 1][start_col + j]==0:
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
                if ans[i][j]==0:
                    countComp=0
                if countComp==4:
                    return True
        
        return False