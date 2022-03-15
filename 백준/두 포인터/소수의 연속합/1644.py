import sys
import math

input = sys.stdin.readline

def solve(m):
  #소수 구하기
  array = [True for _ in range(m+1)]
  primes = []
  for i in range(2, int(math.sqrt(m))+1):
    j = 2
    while i * j <= m:
      array[i * j] =False
      j +=1
  for i in range(2, len(array)):
    if array[i]:
      primes.append(i)
  #연속 합 구하기
  end = 0
  count = 0
  sum_value = 0
  n = len(primes)
  for start in range(n):
    while end < n and sum_value < m:
      sum_value += primes[end]
      end += 1
    if sum_value == m:
      count += 1
    sum_value -= primes[start]
  return count

n= int(input())
result = solve(n)
print(result)
