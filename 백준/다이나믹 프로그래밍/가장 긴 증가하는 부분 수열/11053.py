import sys
input =sys.stdin.readline

n = int(input())

d = [1] * (n)
array = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j]+1)
print(max(d))