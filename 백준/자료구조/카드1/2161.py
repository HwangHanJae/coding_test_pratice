import sys
from collections import deque

q = deque()
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    q.append(i)

while True:
    if len(q) ==1:
        print(q[0])
        break
    a = q.popleft()
    print(a, end=' ')
    b = q.popleft()
    q.append(b)