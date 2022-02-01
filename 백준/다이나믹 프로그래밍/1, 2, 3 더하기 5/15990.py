import sys

input = sys.stdin.readline
m = 1000000009

d = [[0] * 4 for _ in range(100000 + 1)]
d[1][1] = 1
d[2][2] = 1
d[3][3] = 1
d[3][1] = 1
d[3][2] = 1
for i in range(4, 100000+1):
    d[i][1] = (d[i-1][2] + d[i-1][3]) % m
    d[i][2] = (d[i-2][1] + d[i-2][3]) % m
    d[i][3] = (d[i-3][1] + d[i-3][2]) % m

n = int(input())
for _ in range(n):
    case = int(input())
    print(sum(d[case]) % m)