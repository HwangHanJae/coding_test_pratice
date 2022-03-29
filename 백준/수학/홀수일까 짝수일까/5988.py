import sys

input =sys.stdin.readline

t = int(input())
for _ in range(t):
  data = int(input())
  if data % 2== 0:
    print('even')
  else:
    print('odd')