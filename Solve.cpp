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
void printArray(int arr[], int n);
bool solve(int (*board)[9][9]);

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

  if(solve(&board)){
    printBoard(board);
  } else {
    printf("Board couldn't be solved\n");
  }
  return 0;
}

void printArray(int arr[], int n){
  printf("[");
  for(int i = 0; i < n; i++){
    printf(" %d,", arr[i]);
  }
  printf("]\n");
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

bool solve(int (*board)[9][9]){
  // todo: should i keep a count to know when im done?
  for(int i = 0; i < 9; i++){
    for(int j = 0; j < 9; j++){
      // currently iterating through all values
      if((*board)[i][j] == 0){  // needs a value
	
	// find un-used values 
	int used[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};  // bool val for used or not
	for(int k = 0; k < 9; k++){
	  if((*board)[i][k] != 0) {  // look at current row
	    used[k] = 1;
	  }
	  if((*board)[k][j] != 0){  // look at current col
	    used[k] = 1;
	  }
	}
	int a = i - (i%3); // left of 3x3 square (row)
	int b = j - (j%3); // top of 3x3 square (col)
	printf("%d %d : 3x3 ", a, b); // debugging
	for(int k = a; k < a+3; k++){
	  for(int l = b; l < b+3; l++){
	    printf("%d", (*board)[k][l]); // debugging
	    int z = (*board)[k][l];
	    if(z != 0){  // look at 3x3
	      used[z-1] = 1;
	    }
	  }
	}
	printf(" end 3x3\n"); // debugging
	printArray(used, 9); // debugging
	for(int k = 0; k < 9; k++){  // try out non-used values
	  if(used[k] != 0){  // not valid value
	    continue;
	  }
	  (*board)[i][j] = k+1;
	  if(i == 8 && j == 8){  // base case (last num found)
	    return true;
	  }
	  printBoard(*board); // debugging
	  if(solve(board)){  // sol found!
	    return true;
	  }
	}
      }
    }
  }
  return false;
}
