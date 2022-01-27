from re import X
import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

def is_prime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
count = 0
for i in array:
    if is_prime(i):
         count += 1

print(count)

