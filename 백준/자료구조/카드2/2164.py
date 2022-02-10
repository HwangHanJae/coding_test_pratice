import sys
from collections import deque
imput = sys.stdin.readline
q = deque()
n = int(input())
for i in range(1, n+1):
    q.append(i)

while True:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    value = q.popleft()
    q.append(value)