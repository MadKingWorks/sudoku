"""
RS:05/01/2025
A sudoku puzzle exists in a txt file and that needs to be solved
Ex:
Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
"""
from itertools import cycle
def read_puzzle(filename) :
    "read a puzzle from a file, file must have only one puzzle"
    puzzle = []
    with open(filename,'r') as file:
        for line in file:
            puzzle.append(line.split('\n')[0])
    print(puzzle)
    return puzzle

puzzle = read_puzzle('puzzle.txt')

def row_valid(puzzle,row,num):
    'check puzzle to see if a number can fit'
    if str(num) in puzzle[row]:
        return False
    return True

def col_valid(puzzle , col,num):
    'check col to see if a number can fit '
    for i in range(len(puzzle[0])):    #traverse across each row
        if puzzle[i][col] == str(num):
            return False
    return True

def box_valid(puzzle,row,col,num):
    'check col to see if a number can fit '
    #get the base address of the box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row):
        for j in range(box_col):
            if puzzle[i][j] == str(num):
                return False

    return True

for i in range(len(puzzle[0])):
    print(puzzle[i])

def test(puzzle,row,col,num):
    print(" The row to be checked is ")
    print(puzzle[0])
    print("The number to be checked in the above row is ",num)
    if row_valid(puzzle,row,num):
        print(f"The {num} fits the above row")
    else:
        print(f"The {num} does not fit the row")


    print(" The col to be checked is ")
    for i in range(len(puzzle[0])):
        print(puzzle[i][col])
    print("The number to be checked in the above col is ",num)
    if col_valid(puzzle,col,num):
        print(f"The {num} fits the above col")
    else:
        print(f"The {num} does not fit the above col")

def replace(item,value,pos):
    temp = list(item)
    temp[pos]=str(value)
    return ''.join(temp)

#test(puzzle,0,0,9)

def check_num_in_position(puzzle,row,col,num):
    if row_valid(puzzle,row,num):
        if col_valid(puzzle,col,num):
            if box_valid(puzzle,row,col,num):
                return True
    return False

def solve(puzzle):
    options = [i for i in range(1,len(puzzle[0])+1)]
    print(options)

    #check each number in sudocu which is 0
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle[0])):
            if str(puzzle[i][j]) == str(0):
                #try a option at this place:
                for value in options:
                    print(f"Trying {value} in pos {i}{j}")
                    if check_num_in_position(puzzle,i,j,value):
                        #if the value satisfies a position, substitute
                        #print(puzzle[i][j]) 
                        replace(puzzle[i],value,j)
                    #else:
                    #    check_num_in_position(puzzle,i,j

solve(puzzle)

print("--------------------------------------")
for i in range(len(puzzle[0])):
    print(puzzle[i])


