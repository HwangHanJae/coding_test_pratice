import sys
import math
input = sys.stdin.readline

def prime_number(m, n):
    array = [True for _ in range(n+1)]
    prime = []
    for i in range(2, int(math.sqrt(n))+1):
        j=2
        while i * j <= n:
            array[i*j] = False
            j+=1
    for num in range(m, n+1):
        if num == 1:
            pass
        elif array[num]:
            prime.append(num)
    return prime

m = int(input().rstrip())
n = int(input().rstrip())
results = prime_number(m,n)
if results == []:
    print(-1)
else:
    print(sum(results))
    print(results[0])
