import random

# Create a 9x9 grid filled with 0s (empty cells)
grid = [[0 for _ in range(9)] for _ in range(9)]

# Helper function to check if a number can be placed at a given cell
def can_place(grid, row, col, num):
    # Check if the number is already in the given row
    if num in grid[row]:
        return False

    # Check if the number is already in the given column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid containing the given cell
    subgrid_row = row // 3
    subgrid_col = col // 3
    for i in range(subgrid_row * 3, subgrid_row * 3 + 3):
        for j in range(subgrid_col * 3, subgrid_col * 3 + 3):
            if grid[i][j] == num:
                return False

    # If none of the above checks fail, we can place the number at the given cell
    return True

# Generate an unsolved Sudoku puzzle by making a random number of random moves
def generate_unsolved_sudoku():
    # Make a random number of random moves (50-70 moves should be enough)
    num_moves = random.randint(50, 70)
    for _ in range(num_moves):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if can_place(grid, row, col, num):
            grid[row][col] = num

    # Print the generated puzzle
    for row in grid:
        print(row)

# Generate and print an unsolved Sudoku puzzle
generate_unsolved_sudoku()
