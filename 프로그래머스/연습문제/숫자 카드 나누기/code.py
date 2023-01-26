from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    n = len(arrayA)
    result = []
    gcd_A = reduce(lambda x, y : gcd(x, y), arrayA, 0)
    gcd_B = reduce(lambda x, y : gcd(x, y), arrayB, 0) 
    for i in range(n):
        if arrayB[i] % gcd_A == 0:
            break
    else:
        result.append(gcd_A)
    for i in range(n):
        if arrayA[i] % gcd_B == 0:
            break
    else:
        result.append(gcd_B)
        
    if len(result) == 0:
        return 0
    else:
        return max(result)
            
            