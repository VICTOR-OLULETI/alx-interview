
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
    while (len(result[i][0]) < n):
        print(result)
        if (len(result[i][0] * 2) <= n):
            result[i + 1] = [result[i][0] * 2, result[i][0]]
            count += 2
        elif (len(result[i][0] + result[i][1]) < n):
            result[i + 1] = [result[i][0] + result[i][1], result[i][1]]
            count += 1
        elif (len(result[i][0] + result[i][1]) == n):
            result[i + 1] = [result[i][0] + result[i][1], result[i][1]]
            # print(result)
            count += 1
        else:
            j = i - 1
            count -= 1
            # storing values up
            
            # check if j is a positive number then
            if (j < 0):
                return (0)
            # check the present and previous entry
            if (result[i][1] == result[j][1]):
                print(f"value of j {j}")
                j = j - 1
                count -= 1
                i = i - 1
            if (len(result[j][0] + result[j][1]) < n):
                result[j + 1] = [result[j][0] + result[j][1], result[j][1]]
            i = i - 1
        i = i + 1
    return count

# print(minOperations(19170307))
print(minOperations(9))


def mOperations(n):
    """
    This function uses prime factors to get the minimum number of operations
    for 'n' 'H'
    n: int
    """
    if not (isinstance(n, int) and n > 0) or (n == 1):
        return (0)
    # counts number of operations
    count = 0
    # d is the prime factor, starting with 2
    d = 2
    while n > 1:
        while n % d == 0:
            count += d 
            n = n / d
        d += 1
    
    return count
print(mOperations(7))