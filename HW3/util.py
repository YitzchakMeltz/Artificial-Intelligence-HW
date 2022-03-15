EMPTY = 0

def iter_column(PLAYER, matrix, seq_len, val):
    max_col = len(matrix[0])
    max_row = len(matrix)
    cols = [[] for _ in range(max_col)]
    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(matrix[y][x])
    return cols

def iter_row(PLAYER, matrix, seq_len, val):
    max_col = len(matrix[0])
    max_row = len(matrix)
    rows = [[] for _ in range(max_row)]
    for x in range(max_col):
        for y in range(max_row):
            rows[y].append(matrix[y][x])
    return rows

def iter_upward_diagonal(PLAYER, matrix, seq_len, val):
    max_col = len(matrix[0])
    max_row = len(matrix)
    udiag = [[] for _ in range(max_row + max_col - 1)]
    for x in range(max_col):
        for y in range(max_row):
            udiag[x+y].append(matrix[y][x])
    return udiag

def iter_downward_diagonal(PLAYER, matrix, seq_len, val):
    max_col = len(matrix[0])
    max_row = len(matrix)
    min_bdiag = -max_row + 1
    ddiag = [[] for _ in range(max_row + max_col - 1)]
    for x in range(max_col):
        for y in range(max_row):
            ddiag[x-y-min_bdiag].append(matrix[y][x])
    return ddiag

def count_consecutive(PLAYER, matrix, seq_len, val):
    for row in matrix:
        count = 0
        for column in row:
            if column == PLAYER:
                count += 1
            if column != PLAYER:
                count = 0
            if count == seq_len:
                return val
    return 0

def empty_slots(direction, matrix, seq_len, i, j):
    slots = 0
    if j-seq_len >= 0 and matrix[i][j-seq_len] == EMPTY:
        slots += 1
    if j < len(matrix[i])-1 and matrix[i][j+1] == EMPTY:
        slots += 1
    return slots

print(iter_downward_diagonal(0,[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0,0))