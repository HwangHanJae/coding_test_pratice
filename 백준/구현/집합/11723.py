import sys

input =sys.stdin.readline
sets = set()
all = set([i for i in range(1,21)])

for _ in range(int(input())):
  data = list(map(str, input().split()))
  if data[0] == "add":
    sets.add(int(data[1]))
  elif data[0] == "remove":
    if int(data[1]) in sets:
      sets.remove(int(data[1]))
    else: 
      pass
  elif data[0] == "toggle":
    if int(data[1]) in sets:
      sets.remove(int(data[1]))
    else:
      sets.add(int(data[1]))
  elif data[0] == "all":
      sets = all
  elif data[0] == "empty":
    sets.clear()
  elif data[0] == "check":
    if int(data[1])  in sets:
      print(1)
    else:
      print(0) 