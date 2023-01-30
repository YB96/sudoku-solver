import copy
import numpy as np

puzzle1 =  [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
           [6, 0, 0, 1, 9, 5, 0, 0, 0], 
           [0, 9, 8, 0, 0, 0, 0, 6, 0], 
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def get_row(sudoku, k):
    return sudoku[k]

def get_col(sudoku, k):
    result = []                        #we made a null-list as we need a list as an output
    for i in range(9):                 #using range to make sure it work on all the columns
        result.append(sudoku[i][k])    #using .append to add every i and k at the end
        
    return result


def get_box(sudoku, k):
    

    if k == 0:
        a, b = 0, 0
    elif k == 1:
        a, b = 0, 3
    elif k == 2:
        a, b = 0, 6
    elif k == 3:
        a, b = 3, 0
    elif k == 4:    
        a, b = 3, 3
    elif k == 5:    
        a, b = 3, 6
    elif k == 6:    
        a, b = 6, 0
    elif k == 7:    
        a, b = 6, 3
    elif k == 8:    
        a, b = 6, 6
    return sudoku[a][b:b+3] + sudoku[a+1][b:b+3] + sudoku[a+2][b:b+3]

def first_empty_position(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None

def is_section_valid(nums):
    for digit in range(1,10):
        if nums.count(digit) > 1:
            return False
    return True  

def is_sudoku_valid(sudoku):
    rows_valid = all([is_section_valid(get_row(sudoku, i)) for i in range(0, 9)])
    cols_valid = all([is_section_valid(get_col(sudoku, i)) for i in range(0, 9)])
    boxes_valid = all([is_section_valid(get_box(sudoku, i)) for i in range(0, 9)])
    return rows_valid and cols_valid and boxes_valid

def is_section_complete(nums):
    for digit in range (1,10):
        if nums.count(digit) != 1:
            return False
    return True    

def is_sudoku_complete(sudoku):
    rows_complete = all([is_section_complete(get_row(sudoku, i)) for i in range(0, 9)])
    cols_complete = all([is_section_complete(get_col(sudoku, i)) for i in range(0, 9)])
    boxes_complete = all([is_section_complete(get_box(sudoku, i)) for i in range(0, 9)])
    return rows_complete and cols_complete and boxes_complete

def repeat(sudoku):
    # Check if Sudoku is already complete
    if is_sudoku_complete(sudoku):
        return True
    
    # Find the first empty position
    i, j = first_empty_position(sudoku)
    
    # Try to fill it with numbers 1 to 9
    for digit in range(1, 10):
        
        # Insert the digit into the right place
        sudoku[i][j] = digit
        
        # Check if the new puzzle is valid
        if is_sudoku_valid(sudoku):
            
            # Try to fill the remaining spaces recursively using `repeat`
            # Node that this will directly fill values into the sudoku
            result = repeat(sudoku)
            
            # If the recursive result is true, we have found the answer and filled the sudoku
            if result is True:
                return True
        
        
        # Remove the digit, it doesn't lead to a solution
        sudoku[i][j] = 0
        
    
    # There are no valid numbers to fill the empty slot(s)
    return False



def solve_sudoku(sudoku):
    # Create a deep copy of the puzzle (list of lists),
    # to avoid modifying the original
    copied_sudoku = copy.deepcopy(sudoku)
    
    # Try to complete the Sudoku using repeat
    result = repeat(copied_sudoku)
    
    # Return the solved version if successful
    if result is True:
        return copied_sudoku
    
    # Return None if unsuccessful
    return None    

solved_puzzle = solve_sudoku(puzzle1)



print(np.matrix(solved_puzzle))