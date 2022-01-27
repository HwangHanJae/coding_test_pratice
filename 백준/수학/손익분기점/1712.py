import math
import sys

a, b, c = map(int, sys.stdin.readline().split())
if a == 0 or c<=b:
    print(-1)
else:
    point =  a // (c - b)
    print(math.ceil(point)+1)