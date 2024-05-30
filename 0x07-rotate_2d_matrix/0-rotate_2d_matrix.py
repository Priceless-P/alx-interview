#!/usr/bin/python3
"""Rotate 2D Matrix"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """Rotate n x n 2D matrix 90 degrees
    clockwise"""
    n = len(matrix)

    # Transpose in place
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row],\
                                                 matrix[row][col]

        # Reverse in place
        matrix[row].reverse()
