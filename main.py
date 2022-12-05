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
def generate_unsolved_sudoku(difficulty):
    # Make a random number of random moves
    num_moves = random.randint(50, 70)
    if difficulty == "easy":
        num_moves -= 10
    elif difficulty == "hard":
        num_moves += 10

    for _ in range(num_moves):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if can_place(grid, row, col, num):
            grid[row][col] = num

    # Print the generated puzzle
    for row in grid:
        print(row)

# Main program loop
while True:
    # Generate and print an unsolved Sudoku puzzle of the given difficulty level
    difficulty = input("Enter the desired difficulty level (easy, medium, or hard) or 'exit' to quit: ")
    if difficulty == "exit":
        break
    generate_unsolved_sudoku(difficulty)

    # Ask the user if they want to try another puzzle or change the difficulty level
    choice = input("Enter 'again' to try another puzzle or 'change' to change the difficulty level: ")
    if choice == "change":
        continue
    elif choice == "again":
        continue
    else:
        break
