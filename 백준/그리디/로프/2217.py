import sys
input = sys.stdin.readline
array = []
value = []
n = int(input())
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)

for i in range(n):
    value.append(array[i]*(i+1))
print(max(value))