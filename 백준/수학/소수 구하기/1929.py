import math
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

def prime(m,n):
    array = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] =False
                j += 1
    return array
array = prime(m,n)
for i in range(m,len(array)):
    if i == 1:
        pass
    else:
        if array[i]:
            print(i)
