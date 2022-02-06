import sys

input = sys.stdin.readline

t = int(input().rstrip())
num = 14
    
d = [[0 for _ in range(num+1)] for _ in range(num+1)]

for i in range(num+1):
    for j in range(num+1):
        if i == 0:
            d[i][j] = j
        elif j == 0:
            d[i][j] = 0
        else:
            d[i][j] += d[i-1][j]+d[i][j-1]
for _ in range(t):
    k = int(input())
    n = int(input())
    print(d[k][n])