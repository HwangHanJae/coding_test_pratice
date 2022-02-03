import sys
input =sys.stdin.readline

n = int(input())

d = [1] * n

array = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j]+1)
print(max(d))

max = max(d)
result  = []
for i in range(n-1, -1, -1):
    if d[i] == max:
        result.append(array[i])
        max -= 1
result.reverse()
for i in range(len(result)):
    print(result[i], end=' ')