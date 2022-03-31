import sys

input =sys.stdin.readline

for i in range(int(input())):
  stack = []
  result = ''
  array = list(map(str, input().split()))
  for word in array:
    stack.append(word)
  while stack:
     result += stack.pop()
     result += ' '
  print("Case #{}: {}".format(i+1, result.rstrip()))