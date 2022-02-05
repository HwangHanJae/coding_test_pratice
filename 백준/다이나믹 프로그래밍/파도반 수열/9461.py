import sys

input = sys.stdin.readline

n = 100
d = [0 for _ in range(100+1)]
for i in range(1, n+1):
    if i <= 3:
        d[i] = 1
    else:
        d[i] = d[i-3] + d[i-2]

t = int(input())
for _ in range(t):
    case = int(input())
    print(d[case])