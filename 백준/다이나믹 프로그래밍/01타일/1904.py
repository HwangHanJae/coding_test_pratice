import sys

input = sys.stdin.readline

n = int(input())
m = 15746
d = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        d[i] = i % m
    elif i == 2:
        d[i] = i % m
    else:
        d[i] = d[i-1] % m + d[i-2] % m

result = d[n] % m
print(result)
