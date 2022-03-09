import sys

input =sys.stdin.readline

n, m = map(int, input().split())

up = [0] * (n+1)

up[n] = n

for i in range(n-1, n-m, -1):
  up[i] = up[i+1] * i

down = [1] * (m+1)
down[0] = 1
for i in range(1, m+1):
  down[i] = down[i-1] * i


print(up[n-m+1] // down[m])