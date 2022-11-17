import math
def solution(number, limit, power):
    
    len_divisors = []
    result = 0
    for n in range(1, number+1):
        len_divisors.append(get_len_divisor(n))
    for a in len_divisors:
        if a <= limit:
            result += a
        else:
            result += power
    return result
def get_len_divisor(n):
    result = []
    
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if (i ** 2) != n:
                result.append(n // i)
    return len(result)