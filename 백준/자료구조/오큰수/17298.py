import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

stack = deque()
result = [-1] * n

stack.append(0)
i = 1

while stack and i < n:
    while stack and array[stack[-1]] < array[i]:
        result[stack[-1]] = array[i]
        stack.pop()

    stack.append(i)
    i+=1

for i in result:
    print(i , end=' ')