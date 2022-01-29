
import sys

def tiling(x):
    d = [0] * (x+1)

    for i in range(1, x+1):
        if i == 1:
            d[i] = i
        elif i == 2:
            d[i] = i
        if i > 2:
            d[i] = d[i-1] + d[i-2]
    return d[x] % 10007

input = sys.stdin.readline

n = int(input())

result = tiling(n)
print(result)