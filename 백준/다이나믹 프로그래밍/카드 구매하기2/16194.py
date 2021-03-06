import sys

input = sys.stdin.readline

n = int(input())

p = [0] + list(map(int, input().split()))
d = [False] * (n+1)

for i in range(1, len(p)):
    for j in range(1, i+1):
        if d[i] == False:
            d[i] = d[i-j] + p[j]
        else :
            d[i] = min(d[i], d[i-j] + p[j])
print(d[n])