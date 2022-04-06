import sys
import math
input =sys.stdin.readline
n = int(input())
for i in list(str(math.factorial(n))[::-1]):
  if i == "0":
    pass
  else:
    print(i)
    break