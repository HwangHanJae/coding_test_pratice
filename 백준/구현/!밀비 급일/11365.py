import sys

input = sys.stdin.readline

while True:
  data = list(map(str,input().split()))
  result = ''
  if data[0] == "END":
    break
  data.reverse()
  for word in data:
    result += word[::-1]
    result += ' '
  print(result.rstrip())
    