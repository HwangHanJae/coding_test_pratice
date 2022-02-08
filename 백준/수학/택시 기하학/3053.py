import sys
from math import pi as pi
input = sys.stdin.readline


r = int(input())

def result1(r):
    return round(pi * r**2,6)


def result2(r):
    d = abs(r-0) + abs(r-0)
    return d*r


print(result1(r))
print(result2(r))