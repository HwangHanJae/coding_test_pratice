import sys

input = sys.stdin.readline

n = int(input())

d = [0 for _ in range(90+1)]
d[1] = 1
d[2] = 1
for i in range(3, 90+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])