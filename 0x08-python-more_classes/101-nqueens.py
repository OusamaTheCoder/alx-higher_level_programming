#!/usr/bin/python3
"""
N queens problem solution
Usage: nqueens N
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in a given cell (row, col).
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N queens problem using backtracking.
    """
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0  # backtrack


def print_solution(board):
    """
    Print the solution.
    """
    queens_positions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                queens_positions.append([i, j])
    print(queens_positions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = [[0] * N for _ in range(N)]

    solve_nqueens(chessboard, 0, N)
