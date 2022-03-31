import sys

input =sys.stdin.readline

stack = []
n = int(input())
for i in range(n):
  data = int(input())
  stack.append(data)


bar = stack.pop()
count = 1
while stack:
  next_bar = stack.pop()
  if bar < next_bar:
    count +=1
    bar = next_bar
print(count)