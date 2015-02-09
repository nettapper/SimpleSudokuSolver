print("Starting Up...")

board = [[0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0]]

assert(len(board) == 9)  # num of rows must be 9
for i in range(9):
    assert(len(board[i]) == 9)  # num of cols needs to be 9 for each row


print("Div and Conq:")

def solve(board):
    # get our x and y position
    x,y = getNext(board)
    if(x == -1 or y == -1):
        return True  # no more empty positions

    for n in range(1,10):
        if(isValid(board, x, y, n)):
            board[x][y] = n  # try n
            solve(board)
            board[x][y] = 0  # n didn't work try next
    return False

def getNext(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if(board[x][y] == 0):
                return x,y
    return -1,-1

def isValid(board, i, j, n):
    # check row
    for x in range(len(board[i])):
        current = board[i][x]
        if (current == n): return False
    # check col
    for x in range(len(board)):
        current = board[x][j]
        if (current == n): return False
    # check 3x3 box
    a = i // 3
    b = j // 3
    for x in range(a*3, (a+1)*3):
        for y in range(b*3, (b+1)*3):
            current = board[x][y]
            if (current == n): return False
    return True

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

print("Original Board:")
printBoard(board)
print("")
solve(board)
print("")
print("Solved Board:")
printBoard(board)
