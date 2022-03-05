import sys

input = sys.stdin.readline

def solve(n):
  array = []
  for i in n:
    array.append(i)
  left = []
  right = []
  
  for i in range(int(len(array)/2)):
    left.append(array[i])
  array.reverse()
  for i in range(int(len(array)/2)):
    right.append(array[i])
  return left, right
while True:
  n = input().rstrip()
  if int(n) == 0:
    break
  left, right = solve(n)
  if left == right:
    print("yes")
  else:
    print('no')
  