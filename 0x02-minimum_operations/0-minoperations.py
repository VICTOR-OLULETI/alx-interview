#!/usr/bin/env python3
"""
    This program checks the the minimum number of 
    operation to get 'n' 'H'
"""
result = {}
def minOperations(n):
    """
        this function checks the min operations required
        n: int
    """
    if not (isinstance(n, int) and n > 0):
        return 0
    result[0] = ['H', '']
    i = 0
    count = 0
    #for i in range(n):
    while (len(result[i][0]) < n):
        print(result)
        if (len(result[i][0] * 2) < n):
            result[i + 1] = [result[i][0]* 2, result[i][0]]
            count += 2
        elif (len(result[i][0] + result[i][1]) < n):
            result[i + 1] = [result[i][0] + result[i][1], result[i][1]]
            count += 1
        elif (len(result[i][0] + result[i][1]) == n):
            result[i + 1] = [result[i][0] + result[i][1], result[i][1]]
            print(result)
            count += 1
            #break
        else:
            #check previous entry of 1
            j = i - 1
            count -= 1
            # check if j is a positive number then
            if (len(result[j][0] + result[j][1]) < n):
                result[j + 1] = [result[j][0] + result[j][1], result[j][1]]
            i = i - 1
        i = i + 1
    return count
minOperations(4)