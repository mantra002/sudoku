def print_puzzle(puzzle):
    print("   0 1 2   3 4 5   6 7 8")
    print(" +-------+-------+-------+")
    
    for row in range(9):
        for col in range(9):
            if(col==0): print(row, end='')
            if(col%3 == 0): print("| ", end='')
            if(puzzle[row][col] == -1):
                print(" ", end=' ')
            else:
                print(puzzle[row][col], end=' ')
        print("|")
        if (row+1)%3 ==0: print(" +-------+-------+-------+")

def load_puzzle(filename):
    puzzle = [];
    with open(filename) as f:
        for line in f:
            line = line.rstrip().split(',')
            int_line = []
            for s in line:
                if s == '_' or s == ' ':
                    int_line.append(-1)
                else: 
                    int_line.append(int(s))
            puzzle.append(int_line)
    return puzzle

# Function to check if it's safe to place a number in a given position
def is_valid(puzzle, row, col, num):
    # Check the row
    for i in range(N):
        if puzzle[row][i] == num:
            return False
    
    # Check the column
    for i in range(N):
        if puzzle[i][col] == num:
            return False
    
    # Check the quadrant
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(puzzle):
    # Find an empty space (denoted by -1)
    empty = find_empty_location(puzzle)
    if not empty:
        return True  # Puzzle is solved
    
    row, col = empty

    # Try numbers 1 to 9
    for num in range(1, N + 1):
        if is_valid(puzzle, row, col, num):
            # Place the number
            puzzle[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(puzzle):
                return True

            # Backtrack if placing the number doesn't lead to a solution
            puzzle[row][col] = -1

    return False  # No solution found

# Function to find an empty location (denoted by -1)
def find_empty_location(puzzle):
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == -1:
                return (i, j)
    return None

filename = "sudoku_hard.txt"
N=9
puzzle = load_puzzle(filename)

# Solve the Sudoku and print the solution
if solve_sudoku(puzzle):
    print("Sudoku solved successfully!")
    print_puzzle(puzzle)
else:
    print("No solution exists.")

