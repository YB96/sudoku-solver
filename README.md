# Sudoku Solver

## Sudoku is a logic-based, number-placement puzzle. The objective is to fill a 9x9 grid with numbers so that each column, each row, and each of the nine 3x3 sub-grids that compose the grid contain all of the digits from 1 to 9.

Let's automate it through **Python**

We are going to use **NumPy** library for this project.<br>
*Note: Pass the codes in terminal or you can use jupyter notebook*

<code>!pip install pandas numpy </code>

Now lets import the required libraries

<code>import numpy as np </code>

Passing the desired **Sudoku** as a nested list.<br>
*A nested list in Python is a list that contains one or more lists as its elements. These inner lists can contain any type of data, including other lists, which can be nested to any depth.*
<br>
<code>grid =  [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
           [6, 0, 0, 1, 9, 5, 0, 0, 0], 
           [0, 9, 8, 0, 0, 0, 0, 6, 0], 
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]
</code>
<br>
*We has passed zero to the digits we need to discover.*<br>

<code>def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range (0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3 
    for i in range(0,3):
        for j in range (0,3):
            if grid[y0+i] [x0+j] == n:
                return False
    return True                          
</code>
<br>
<code>def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x]= 0   
                return   </code>               

<code>print(np.matrix(grid))
    input('More?')   #press enter at more to find more possible solutions.
solve()               </code>


### This code will help you get multiple results of a Sudoku.
*Raw file can be find here also*
## Thank you for visiting.

