def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col, n):
    # Check the column
    i = 0
    while i < row:
        if board[i][col]:
            return False
        i += 1

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True



def solve_n_queens_util(board, row, n, solutions):
    # If all queens are placed, add the solution to the list
    if row == n:
        solutions.append([row[:] for row in board])
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            solve_n_queens_util(board, row + 1, n, solutions)  # Recurse
            board[row][col] = 0  # Backtrack


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the chessboard
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)  # Solve the problem
    return solutions


# Example usage
n = int(input("Enter number of Queens - ")) 
solutions = solve_n_queens(n)

print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for index, solution in enumerate(solutions, start=1):
    print(f"Solution {index}:")
    print_solution(solution)