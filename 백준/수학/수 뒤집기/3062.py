import sys

input =sys.stdin.readline
t = int(input())
for _ in range(t):
  data = input().rstrip()
  value = int(data) + int(data[::-1])
  if str(value) == str(value)[::-1]:
    print("YES")
  else:
    print('NO')