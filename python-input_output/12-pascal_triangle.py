#!/usr/bin/python3
"""
This module defines function that returns Pascal's triangle of n rows.

Each row is represented as list of integers.
If n <= 0, an empty list is returned.
"""


def pascal_triangle(n):
    """
    Generates Pascal triangle up to the nth row.

    Args:
        n (int): number of rows of the triangle to generate.

    Returns:
        list: list of lists of integers representing Pascal triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev = triangle[i - 1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle
