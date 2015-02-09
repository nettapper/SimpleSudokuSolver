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

def solveV2(board, x=0, y=0):
    assert(board[x][y] == 0)  # must be an unkown val to start
    # sol has 81 squares that are not 0's
    isSoln = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                isSoln = False  # a val was not found!
                break
            if(getPoss(board, x, y) != 0):
                isSoln = False  # nothing can be inserted incorrectly
                break
    if(isSoln): return True
    # find possible vals for board[x,y]
    possible = getPoss(board, x, y)
    if(len(possible) == 0): return False
    for val in possible:
        board[x][y] = val
        # then inc the x or y vals to a non-zero
        i, j = x, y
        while(board[i][j] != 0):
            j += 1
            if(j >= len(board[i])):
                i += 1
                j %= len(board[i])
        solveV2(board, i, j)
    return False

def solve(board):
    # debugging
    print("**")
    printBoard(board)
    print("**")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                possible = getPoss(board, i, j)
                if (len(possible) == 0):  # no good vals left
                    return False
                for x in range(len(possible)):  # todo: check to is possible vals are still possible!!
                    board[i][j] = possible[x]
                    if(solve(board)):
                        return True
                return False  # the loop exited -> no vals left to try
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                return False  # a val was not found!
    return True

def getPoss(board, i, j):
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

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

print("Original Board:")
printBoard(board)
print("")
solveV2(board)
print("")
print("Solved Board:")
printBoard(board)
