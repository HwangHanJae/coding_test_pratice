import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d = [-1000] * (n+1)
d[0] = max(array[0], d[0])

for i in range(1, n):
    d[i] = max(array[i], array[i] + d[i-1])
print(max(d))