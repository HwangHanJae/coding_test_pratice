import sys
input =sys.stdin.readline
a,b = map(int,input().split())
if a > b:
  a, b = b, a

result = (a+b)*(b-a+1)
result = result // 2
print(result)