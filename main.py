import random

# Helper function to check if a number can be placed at a given cell
def can_place(grid, row, col, num, n):
    # Check if the number is already in the given row
    if num in grid[row]:
        return False

    # Check if the number is already in the given column
    for i in range(n):
        if grid[i][col] == num:
            return False

    # Check if the number is already in the subgrid containing the given cell
    subgrid_size = int(n ** 0.5)
    subgrid_row = row // subgrid_size
    subgrid_col = col // subgrid_size
    for i in range(subgrid_row * subgrid_size, subgrid_row * subgrid_size + subgrid_size):
        for j in range(subgrid_col * subgrid_size, subgrid_col * subgrid_size + subgrid_size):
            if grid[i][j] == num:
                return False

    # If none of the above checks fail, we can place the number at the given cell
    return True

# Generate an unsolved Sudoku puzzle by making a random number of random moves
def generate_unsolved_sudoku(n, difficulty):
    # Create an nxn grid filled with 0s (empty cells)
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Make a random number of random moves
    num_moves = random.randint(int(n * 0.5), int(n * 0.7))
    if difficulty == "easy":
        num_moves -= int(n * 0.1)
    elif difficulty == "hard":
        num_moves += int(n * 0.1)

    for _ in range(num_moves):
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        num = random.randint(1, n)
        if can_place(grid, row, col, num, n):
            grid[row][col] = num

    # Print the generated puzzle
    for row in grid:
        print(row)

# Main program loop
while True:
    # Generate and print an unsolved Sudoku puzzle of the given difficulty level and grid size
    n = int(input("Enter the size of the grid (e.g. 4 for a 4x4 grid): "))
    difficulty = input("Enter the desired difficulty level (easy, medium, or hard) or 'exit' to quit: ")
    if difficulty == "exit":
        break
    generate_unsolved_sudoku(n, difficulty)

    # Ask the user if they want to try another puzzle or change the difficulty level
    choice = input("Enter 'again' to try another puzzle or 'change' to change the difficulty level: ")
    if choice == "change":
        continue
    elif choice == "again":
        continue
    else:
        break
