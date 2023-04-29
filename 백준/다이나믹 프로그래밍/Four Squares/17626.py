import sys
n = int(sys.stdin.readline())
d = {}
d[0] = 0
d[1] = 1
for i in range(2, n+1):
    min_value = 1e9
    for j in range(1, int(i**0.5) + 1):
        min_value = min(min_value, d[i-j**2])
    d[i] = min_value+1

print(d[n])