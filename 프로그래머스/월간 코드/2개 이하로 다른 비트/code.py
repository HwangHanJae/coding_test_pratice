from collections import deque
def solution(numbers):
    
    result = []
    for number in numbers:
        result.append(f(number))
    return result

def f(x):
    if x % 2 == 0:
        return x+1
    else:
        cur = deque(bin(x)[2:])
        nex = deque(bin(x+1)[2:])
        if len(nex)>len(cur):
            cur.appendleft(0)
        for i in range(len(cur)-1,-1, -1):
            if cur[i] == '0':
                break
        cur[i], cur[i+1] = 1, 0
        return int(''.join(map(str, cur)), 2)
        
    
        