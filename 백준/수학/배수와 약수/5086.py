import sys

input =sys.stdin.readline

def factor(a,b):
  array = []
  for i in range(1, b+1):
    if b % i == 0:
      array.append(b // i)
  for i in array[::-1]:
    if i == a:
      return True
  return False
def multiple(a, b):
  if a % b == 0:
    return True
  return False
while True:
  a, b = map(int,input().split())
  if (a, b) == (0,0):
    break
  if factor(a,b):
    print("factor")
  elif multiple(a, b):
    print("multiple")
  else:
    print("neither")