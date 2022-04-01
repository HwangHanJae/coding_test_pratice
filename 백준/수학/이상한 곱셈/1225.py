import sys

input =sys.stdin.readline

a, b = map(str, input().split())
result = 0
a_sum = 0
for i in a:
  a_sum += int(i)
for j in b:
  result += a_sum * int(j)
print(result)