import sys
import math

def get_prime():
    array = [True for _ in range(1000000+1)]
    for i in range(2, int(math.sqrt(1000000))+1):
        if array[i]:
            j = 2
            while i * j <= 1000000:
                array[i * j] = False
                j +=1
    array[0] = False
    array[1] = False
    return array

prime = get_prime()
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    result = 0
    n = int(input().rstrip())
    for i in range(1, n//2 + 1):
        a = i
        b = n - i
        if prime[a] and prime[b]:
            result+=1
    print(result)