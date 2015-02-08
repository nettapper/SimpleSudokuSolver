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
    # sol has 81 squares that are not 0's
    # find possible vals for board[x,y]
    #   then inc the x or y vals to a non-zero
    pass

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
    # debugging
    print("Above board generated the array below")
    print(vals)
    # return what is left of the array
    return vals

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
