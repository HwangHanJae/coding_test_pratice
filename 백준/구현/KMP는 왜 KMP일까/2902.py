import sys

input = sys.stdin.readline

data = list(map(str, input().split('-')))
result = ""
for i in data:
  result += i[0]
print(result)