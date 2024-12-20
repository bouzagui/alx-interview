#!/usr/bin/python3
""" rotate 2D matrix """


def rotate_2d_matrix(matrix):
    """ rotate 2D matrix

    Args:
        matrix: 2D matrix

    Returns:
        None
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
