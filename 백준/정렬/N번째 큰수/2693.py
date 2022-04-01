import sys

input=sys.stdin.readline
for _ in range(int(input())):
  array = map(int, input().split())
  print(sorted(array, reverse=True)[2])