import sys

input =sys.stdin.readline

t = int(input())
for _ in range(t):
  data = input().rstrip()
  print(data[0]+data[-1])