#!/usr/bin/python3
"""
0-pascal_triange
"""
def pascal_triangle(input):
    """
    This function takes in a number input and computes
    the pascal triangle.
    """
    if input == 0:
        return []

    if input == 1:
        return [[1]]

    result = [[1]]
    for num in range(input - 1):
        if num == 0:
            result.append([1, 1])
        else:
            temp = []
            temp.append(1)
            # check the previous position and add the numbers like a pascal
            temp1 = result[num]
            for i in range(len(temp1) - 1):
                num2 = temp1[i] + temp1[i + 1]
                temp.append(num2)
            temp.append(1)
            result.append(temp)
    return result
