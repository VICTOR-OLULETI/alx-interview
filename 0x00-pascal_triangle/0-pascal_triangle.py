#!/usr/bin/python3
"""
0-pascal_triange
"""


def pascal_triangle(n):
    """
    This function takes in a number input and computes
    the pascal triangle.
    """
    if n == 0:
        return []

    result = [[1]]
    for num in range(n - 1):
        if num == 0:
            result.append([1, 1])
        else:
            new_row = [1]
            # check the previous position and add the numbers like a pascal
            prev_row_length = result[num]
            for i in range(len(prev_row_length) - 1):
                new_row.append(prev_row_length[i] + prev_row_length[i + 1])
            new_row.append(1)
            result.append(new_row)
    return result
