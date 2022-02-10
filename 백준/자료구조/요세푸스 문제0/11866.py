import sys
from collections import deque

q = deque()
input =sys.stdin.readline

n, k = map(int,input().split())

for i in range(1, n+1):
    q.append(i)
    
result = []
while q:
    for i in range(k):
        if i == k-1:
            value = q.popleft()
            result.append(value)
        else:
            num = q.popleft()
            q.append(num)
print('<', end ='')
for i in range(len(result)):
    if i == len(result)-1:
        print(str(result[i]),end='')
    else:
        print(str(result[i]), end=', ')
print(">")