import sys
import math

input =sys.stdin.readline

def is_prime(num):
  array = [True for _ in range(num+1)]
  prime = []
  for i in range(2, int(math.sqrt(num))+1):
    j = 2
    while i * j <= num:
      array[i * j] = False
      j +=1
  for i in range(1, len(array)):
    if array[num]:
      print("It is a prime word.")
      return
    else:
      print("It is not a prime word.")
      return

word  = input().rstrip()
value = 0
for i in word:
  if 65<=ord(i)<=90:
    value += ord(i) - 38
  else:
    value += ord(i) - 96

is_prime(value)