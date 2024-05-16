#!/usr/bin/python3
"""N queens
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at
    the given position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N, board, row):
    """
    Solve the N Queens problem recursively

    Args:
        N (int): The size of the chessboard.
        board (list): The current state of the chessboard.
        row (int): The current row being processed.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, board, row+1)
            board[row] = -1


def main():
    """
    Parse command line arguments .
    """
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

    board = [-1] * N
    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    main()
