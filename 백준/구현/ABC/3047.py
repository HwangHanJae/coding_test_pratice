import sys
input = sys.stdin.readline
data  = list(map(int, input().split()))
array = sorted(data)
result = []
s = input().rstrip()
for i in s:
  if i == "C":
    result.append(array[2])
  elif i == "B":
    result.append(array[1])
  elif i == "A":
    result.append(array[0])

for i in result:
  print(i, end=' ')
