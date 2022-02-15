import sys

input = sys.stdin.readline

result = []
n, k = map(int, input().split())
for i in range(1, n+1):
    if n % i == 0:
        result.append(i)

if len(result) < k:
    print(0)
else:
    print(result[k-1])