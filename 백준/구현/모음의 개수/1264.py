import sys

input = sys.stdin.readline

while True:
  count= 0
  data = input().rstrip()
  if data == "#":
    break
  for i in data:
    if i.lower() in ["a","e","i","o",'u']:
      count +=1
  print(count)