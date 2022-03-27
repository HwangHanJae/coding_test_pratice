import sys
input =sys.stdin.readline

for _ in range(int(input())):
  data = input().rstrip()
  result = ''
  for i in range(len(data)):
    if i == 0:
      result+=data[i].upper()
    else:
      result += data[i]
  print(result)
