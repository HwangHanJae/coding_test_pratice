import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())


x = min(a,b)
#소수 구하기
def is_prime_number(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i *j <=n:
                array[i*j] = False
                j +=1
    return [i for i in range(2, n+1) if array[i]]
primes = is_prime_number(x)

a_copy, b_copy = a, b
fac = 1
mul = 1
#최대 공약수 구하기
for number in primes:
    while (a_copy % number == 0) and (b_copy % number == 0):
        a_copy = a_copy // number
        b_copy = b_copy // number
        fac *= number
            
#최소 공배수 구하기
a_mul = a // fac
b_mul = b // fac
mul = a_mul * b_mul * fac

print(fac)
print(mul)
