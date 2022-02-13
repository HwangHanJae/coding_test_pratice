import sys
import math
input = sys.stdin.readline
m = 10007

n, k = map(int, input().split())
result = math.comb(n,k) % m
print(result)