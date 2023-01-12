from functools import reduce
def solution(data, col, row_begin, row_end):
    s = sorted(data, key = lambda x : (x[col-1], -x[0]))
    numbers = []
    result = 0
    for i in range(row_begin, row_end+1):
        number = sum([n % i for n in s[i-1]])
        numbers.append(number)
        
    result = reduce(lambda x, y : x^y, numbers)
    
    return result