from re import I
import sys

input = sys.stdin.readline
n = 9

array = [0] * n
for x in range(n):
    h = int(input())
    array[x] = h
check = sum(array) - 100

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if (array[i] + array[j]) == check:
            drop_i, drop_j = i, j

result = []
for i in range(len(array)):
    if i == drop_i or i == drop_j:
        pass
    else:
        result.append(array[i])
result = sorted(result)
for i in range(len(result)):
    print(result[i])