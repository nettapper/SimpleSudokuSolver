/*
Create board (9, 9) w/ known values
Copy the array to store known values
Iterate through all 81 positions starting with the top left one
  base case: all 81 pos have a number, return true

  for each pos find the valid vaules (rows, cols, and 3x3 square)
  if there are no valid numbers return false
  try a valid one and call the function again

*/
