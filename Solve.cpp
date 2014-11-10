/*
Create board (9, 9) w/ known values
Copy the array to store known values
Iterate through all 81 positions starting with the top left one
  base case: all 81 pos have a number, return true

  for each pos find the valid vaules (rows, cols, and 3x3 square)
  if there are no valid numbers return false
  try a valid one and call the function again

*/
#include <stdio.h>

void printBoard(int board[9][9]);
bool solve(int board[9][9]);

int main(){
  int board[9][9] = {{0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},		      
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0, 0}};

  if(solve(board)){
    printBoard(board);
  } else {
    printf("Board couldn't be solved\n");
  }
  return 0;
}

void printBoard(int board[9][9]){
  for(int i = 0; i < 9; i++){
    if(i % 3 == 0 & i != 0){  // horz line after rows 2 & 3
      printf("---------------------\n");
    }
    for(int j = 0; j < 9; j++){
      if(j == 2 || j == 5){  // vert line after cols 3 and 6
	printf("%d | ", board[i][j]);
      } else {
	printf("%d ", board[i][j]);
      }
    }
    printf("\n");
  }
}

bool solve(int board[9][9]){
  // do stuff
  return false;
}
