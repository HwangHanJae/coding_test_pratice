import sys
input = sys.stdin.readline

s = list(input())
#a = 97, z = 122
array = [0] * 123


for i in s:
    array[ord(i)] += 1

for i in range(97, 123, 1):
    print(array[i], end=' ')