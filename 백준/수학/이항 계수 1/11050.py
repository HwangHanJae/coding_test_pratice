import sys

input = sys.stdin.readline

def comb(n, k):
    result1 = 1
    result2 = 1
    for i in range(k):
        result1 *= n-i
    for i in range(k, 0 ,-1):
        result2 *= i
    return int(result1 / result2)


n, k = map(int, input().split())
result = comb(n,k)
print(result)

    