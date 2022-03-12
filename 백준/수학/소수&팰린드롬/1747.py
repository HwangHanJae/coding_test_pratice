import sys
import math
input = sys.stdin.readline
def get_primes(n):
  num =1003001
  prime = []
  array = [True for _ in range(num+1)]
  for i in range(2, int(math.sqrt(num))+1):
    j = 2
    while i * j <= num:
      array[i * j] = False
      j += 1
  array[0] = False
  array[1] = False
  for i in range(n, len(array)):
    if array[i]:
      prime.append(i)
  return prime
def get_pal(prime):
  prime = str(prime)
  value = len(prime) // 2
  temp = list(prime)
  left = temp[:value]
  temp.reverse()
  right = temp[:value]
  result = ''
  if left == right:
    for i in temp:
      result += i
    return result
  else:
    return None
n = int(input())
for prime in get_primes(n):
  result = get_pal(prime)
  if result != None:
    print(result)
    break