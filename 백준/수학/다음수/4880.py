import sys
input =sys.stdin.readline

def ap(a,b,c):
  result = 0
  check = False
  diff = b-a
  if c-b == diff:
    result = c+diff
    check = True
  return [check,"AP",result]
def gp(a,b,c):
  result = 0
  check = False
  value = b // a
  if c//b == value:
     result = c * value 
     check= True
  return [check, "GP", result]

while True:
  a, b, c = map(int, input().split())
  if (a,b,c,) == (0,0,0):
    break
  if ap(a,b,c)[0]:
    print(ap(a,b,c)[1],ap(a,b,c)[2])
  else:
    print(gp(a,b,c)[1], gp(a,b,c)[2])
