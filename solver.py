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


print("Div and Conq")

def solve(board, x=0, y=0):
    # debugging
    printBoard(board)
    print("***")
    # end debugging
    assert(board[x][y] == 0)  # must be an unkown val to start
    # sol has 81 squares that are not 0's
    isSoln = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                isSoln = False  # a val was not found!
                break
            for n in range(1,10):
                if(isValid(board, i, j, n)):
                    isSoln = False  # shouldn't have any valid pos left
    if(isSoln): return True
    # find possible vals for board[x,y]
    possible = getPossible(board, x, y)
    if(len(possible) == 0): return False
    for x in range(len(possible)):
        board[x][y] = possible[x]
        # then inc the x or y vals to a non-zero
        i, j = x, y
        while(board[i][j] != 0):
            j += 1
            if(j >= len(board[i])):
                i += 1
                j %= len(board[i])
        solve(board, i, j)
    return False

def getPossible(board, i, j):
    vals = [1,2,3,4,5,6,7,8,9]
    # check row
    for x in range(len(board[i])):
        current = board[i][x]
        try:
            vals.remove(current)
        except ValueError:
            pass
    # check col
    for x in range(len(board)):
        current = board[x][j]
        try:
            vals.remove(current)
        except ValueError:
            pass
    # check 3x3 box
    a = i // 3
    b = j // 3
    for x in range(a*3, (a+1)*3):
        for y in range(b*3, (b+1)*3):
            current = board[x][y]
            # print("c ", current, " | x: ", x, " y: ", y)
            try:
                vals.remove(current)
            except ValueError:
                pass
    # return what is left of the array
    return vals

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
