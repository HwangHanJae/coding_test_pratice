import sys

input = sys.stdin.readline
n = int(input())
result = 0
for _ in range(n):
  a, b, c = map(int, input().split())
  if a == b == c:
    value = 10000 + (a * 1000)
    result = max(result, value)
  elif (a == b) and (c != b):
    value = 1000 + (a * 100)
    result = max(result, value)
  elif (a == c) and (a != b):
    value = 1000 + (a * 100)
    result = max(result, value)
  elif (b == c) and (a != b):
    value = 1000 + (b * 100)
    result = max(result, value)
  elif a != b != c:
    array = [a, b, c]
    value = max(array) * 100
    result = max(result, value)
print(result)