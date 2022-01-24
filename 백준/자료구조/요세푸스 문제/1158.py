from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
array = []
for i in range(1,n+1):
    array.append(i)

numbers = deque(array)
result = []
while numbers:
    for i in range(k-1):
        num=numbers.popleft()
        numbers.append(num)
    result.append(numbers.popleft())

print("<", end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
    else:
        print(result[i], end=", ")
print(">")