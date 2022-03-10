import sys

input =sys.stdin.readline
data = str(input().rstrip())
m = 30
n = []

for i in data:
  n.append(int(i))

n.sort(reverse= True)

number = ''
for i in n:
  number += str(i)

if int(number) % m == 0:
  print(int(number))
else:
  print(-1)
