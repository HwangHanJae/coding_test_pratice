import sys
import math
#소수 구하기
def get_prime(x):
    array = [True for _ in range(x+1)]
    prime = []
    for i in range(2, int(math.sqrt(x))+1):
        if array[i]:
            j = 2
            while i * j <= x:
                array[i * j] = False
                j+=1
    array[0] = False
    array[1] = False
    return array


input = sys.stdin.readline
n =int(input())

prime  = get_prime(n)
while n!=0:
    if n==1:
        break
    for i in range(len(prime)):
        if prime[i]:
            if n % i == 0:
                n = n//i
                print(i)
                break
