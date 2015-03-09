// Sudoku Solver in JS
// def main():
//     print("Starting Up...")
//     board = stringParse("790000300000006900800030076000005002005418700400700000610090008002300000009000054")
// 
//     print("Original Board:")
//     printBoard(board)
//     print("")
//     print("Div and Conq")
//     solve(board)
//     print("")
//     print("Solved Board:")
//     printBoard(board)
//     
var board = [[7,9,0, 0,0,0, 3,0,0],
     [0,0,0, 0,0,6, 9,0,0],
     [8,0,0, 0,3,0, 0,7,6],
     [0,0,0, 0,0,5, 0,0,2],
     [0,0,5, 4,1,8, 7,0,0],
     [4,0,0, 7,0,0, 0,0,0],
     [6,1,0, 0,9,0, 0,0,8],
     [0,0,2, 3,0,0, 0,0,0],
     [0,0,9, 0,0,0, 0,5,4]];

var almost = [[0,1,7, 3,6,9, 8,2,5],  // missing one should be a 4
     [6,3,2, 1,5,8, 9,4,7],
     [9,5,8, 7,2,4, 3,1,6],
     [8,2,5, 4,3,7, 1,6,9],
     [7,9,1, 5,8,6, 4,3,2],
     [3,4,6, 9,1,2, 7,5,8],
     [2,8,9, 6,4,3, 5,7,1],
     [5,7,3, 2,9,1, 6,8,4],
     [1,6,4, 8,7,5, 2,9,3]];

// def stringParse(string):
//     assert(len(string) == 9*9)
//     board = []
//     row, col = -1, 0
//     for col in range(len(string)):
//         if(col % 9 == 0):
//             board.append([0 for _ in range(9)])
//             row += 1
//         val = eval(string[col])
//         board[row][col % 9] = val
//     return board

function solve(board) {
    // my assertions
    if(board.length != 9){
	console.log("Improper length of board rows");
	return null
    }
    for(var i = 0; i < board.length; i++){
	if(board[i].length != 9){
	    console.log("Improper length of board cols");
	    return null
	}
    }
    return solveBackTrack(board);
}

function solveBackTrack(board){
    var next = getNext(board);
    if(next == null){
	return true;  // no more empty positions
    }
    // assert next is len 2
    if(next.length != 2){
	console.log("next position failed");
	return null
    }
    var x = next[0];
    var y = next[1];
    for(var n=1; n<10; n++){
	if(isValid(board, x, y, n)){
	    board[x][y] = n  // try n
	    if(solveBackTrack(board)){
		return true;
	    }
	    board[x][y] = 0;  // n didn't work... need to try a different value
	}
    }
    return false;
}

function getNext(board){
    for(var x=0; x<board.length; x++){
	for(var y=0; y<board[x].length; y++){
	    if(board[x][y] == 0){
		return [x,y];
	    }
	}
    }
    return null;
}

function isValid(board, i, j, n){
    // check row
    for(var x=0; x<board[i].length; x++){
	var current = board[i][x];
	if(current == n){
	    return false;
	}
    }
    // check col
    for(var y=0; y<board.length; y++){
	var current = board[y][j];
	if(current == n){
	    return false;
	}
    }
    // 3x3 box
    var a = Math.floor(i / 3);  // might need to round
    var b = Math.floor(j / 3);
    for(var x=a*3; x<(a+1)*3; x++){
	for(var y=b*3; y<(b+1)*3; y++){
	    var current = board[x][y];
	    if(current == n){
		return false;
	    }
	}
    }
    return true;
}

function printBoard(board) {
    for(var i=0; i < board.length; i++){
        for(var j=0; j < board[i].length; j++) {
            console.log(board[i][j]);
        }
    }
}


// # run the program!
// main()
