
def main():
    print("Starting Up...")
    # board = [  # spacing should make the board more readable
        # [7,9,0, 0,0,0, 3,0,0],
        # [0,0,0, 0,0,6, 9,0,0],
        # [8,0,0, 0,3,0, 0,7,6],
# 
        # [0,0,0, 0,0,5, 0,0,2],
        # [0,0,5, 4,1,8, 7,0,0],
        # [4,0,0, 7,0,0, 0,0,0],
# 
        # [6,1,0, 0,9,0, 0,0,8],
        # [0,0,2, 3,0,0, 0,0,0],
        # [0,0,9, 0,0,0, 0,5,4]]
    board = stringParse("790000300000006900800030076000005002005418700400700000610090008002300000009000054")

    print("Original Board:")
    printBoard(board)
    print("")
    print("Div and Conq")
    solve(board)
    print("")
    print("Solved Board:")
    printBoard(board)
    
def stringParse(string):
    assert(len(string) == 9*9)
    board = []
    row, col = -1, 0
    for col in range(len(string)):
        if(col % 9 == 0):
            board.append([0 for _ in range(9)])
            row += 1
        val = eval(string[col])
        board[row][col % 9] = val
    return board



def solve(board):
    assert(len(board) == 9)  # num of rows must be 9
    for i in range(9):
        assert(len(board[i]) == 9)  # num of cols needs to be 9 for each row

    solveBackTrack(board)

def solveBackTrack(board):
    x,y = getNext(board)
    if(x == -1 or y == -1):
        return True  # no more empty positions
    for n in range(1,10):
        if(isValid(board, x, y, n)):
            board[x][y] = n  # try n
            if(solveBackTrack(board)):
                return True
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


# run the program!
main()
