import sys
import math
#소수 찾기
def prime_number(n):
    array = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            for j in range(i*i, n+1, i):
                array[j] = False
    return array

prime= prime_number(1000000)
while True: 
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    for i in range(3, len(prime)):
        if prime[i] and prime[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break




