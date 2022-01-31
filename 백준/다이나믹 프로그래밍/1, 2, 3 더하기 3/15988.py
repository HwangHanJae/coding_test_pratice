import sys

input = sys.stdin.readline
d = [0] * (1000000+1) 
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 1000000+1):
    d[i] = d[i-3] % 1000000009 + d[i-2] % 1000000009 + d[i-1] % 1000000009

n = int(input())

for _ in range(n):
    case = int(input())
    print(d[case] % 1000000009)