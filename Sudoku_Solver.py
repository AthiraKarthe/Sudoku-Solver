import Playground
SIZE = 9
#sudoku problem
#cells with value 0 are vacant cells
matrix = Playground.sudoku

def print_sudoku():
    for i in matrix:
        print(i)

def next_unsolved_cell(row,col):
    a=[-1,-1,0]
    for i in range(0,SIZE):
        for j in range(0,SIZE):
            if matrix[i][j]==0:
                row=i
                col=j
                a=[row,col,1]
                return a
    return a

def fits(n,r,c):
    for i in range(0,SIZE):
        if matrix[r][i]==n:
            return False
    for i in range(0,SIZE):
        if matrix[i][c]==n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True

def solve():
    row=0
    col=0
    a=next_unsolved_cell(row,col)
    if a[2]==0:
        return True
    row=a[0]
    col=a[1]
    for i in range(1,10):
        if fits(i,row,col):
             matrix[row][col]=i
             if solve():
                 return True
             matrix[row][col]=0
    return False

if solve():
    print_sudoku()
else:
    print("Unsolvable")
