import sys
import math

input = sys.stdin.readline

def get_prime():
    n = 10000
    array = [True for _ in range(n+1)]
    prime = []
    for i in range(2, int(math.sqrt(n)+1)):
        j = 2
        while i * j <=n:
            array[i*j] = False
            j+=1
    return array

primes = get_prime()
t = int(input())
for _ in range(t):
    result = []
    n = int(input())
    for i in range(2,n+1):
        if primes[i] and primes[n-i]:
            diff = abs((n-i)-i)
            result.append((diff, [i, n-i]))
    print(min(result)[1][0], min(result)[1][1])
