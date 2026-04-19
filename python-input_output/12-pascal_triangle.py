#!/usr/bin/python3
"""dfghjk"""


def pascal_triangle(n):
    """fghnm"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        evvelki_row = triangle[i - 1]
        indiki_row = [1]
        for j in range(1, i):
            indiki_row.append(evvelki_row[j - 1] + evvelki_row[j])
        indiki_row.append(1)
        triangle.append(indiki_row)

    return triangle
