import sys
import math

input = sys.stdin.readline
def get_prime():
    number = 123456*2
    array = [True for _ in range(number+1)]
    prime = []
    for i in range(2, int(math.sqrt(number)+1)):
        j = 2
        while i * j <= number:
            array[i*j] = False
            j+=1
    return array

primes = get_prime()
while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(n+1, (2*n)+1):
        if primes[i]:
            count+=1
    print(count)
    