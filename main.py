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

read_puzzle('puzzle.txt')

def solve(puzzle,strategy):

    'solve the sudoku'
    #strategy to solve sudoku is backtracking-Brute force
    if strategy == "Backtracking":
        size_of_puzzle = len(puzzle)
        def check_row(row):
            return True if len({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(row)) == 0   else False
        def check_col(col):
            return True if len({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(col)) == 0 else False
        def check_box(box):
            return True if len(set(set(element for sublist in box for
                                       element in sublist))) == 0 else False
        def get_box(i,j,puzzle):
            quadrant = 0
            if i<=2 :
                if j<=2:
                    quadrant = 0
                elif 3<=j<=5:
                    quadrant = 1
                elif 6<=j<=9:
                    quadrant = 2
            elif 3<=i<=5:
                if j<=2:
                    quadrant = 3
                elif 3<=j<=5:
                    quadrant = 4
                elif 6<=j<=9:
                    quadrant = 5
            else 6<=i<=9:
                if j<=2:
                    quadrant = 6
                elif 3<=j<=5:
                    quadrant = 7
                elif 6<=j<=9:
                    quadrant = 8
            return list()

        masterlist = [1,2,3,4,5,6,7,8,9]
        running = True
        mcycle = cycle(masterlist)
        nextelem = next(mcycle)    #always get next value from list
        for i,row in enumerate(puzzle):
            for j,element in enumerate(row):
                if element == 0 :
                    continue
                saveval = element
                puzzle[i][j] = nextelem
                # get the box
                if check_row(row) and check_col(list(row[0] for row in puzzle)) and check_box([])



