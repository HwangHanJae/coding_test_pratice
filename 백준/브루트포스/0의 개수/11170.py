import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  count = 0
  for i in range(a, b+1):
    for j in str(i):
      if j == "0":
        count+=1
  print(count)