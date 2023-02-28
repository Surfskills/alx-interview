import sys

def isSafe(board, row, col, size): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, size, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True

# Function to print the solution 
def solveNQ(board, col, size): 

    # If all queens are placed then return true 
    if col >= size: 
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by
