import math
from collections import deque
def solution(arr):
    q = deque(arr)
    while len(q) >= 2:
        a = q.popleft()
        b = q.popleft()
        gcd = math.gcd(a, b)
        lcm = (a*b) // gcd
        q.appendleft(lcm)
    return q.popleft()
        
        
        
    

    