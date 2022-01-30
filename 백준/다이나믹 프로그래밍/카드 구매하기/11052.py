import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

p = deque(map(int, input().split()))

d = [0] * (n+1)
p.appendleft(0)

for i in range(1, len(p)):
    for j in range(1, i+1):  
        d[i] = max(d[i], d[i-j] + p[j])
print(d[n])