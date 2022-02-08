import sys
input = sys.stdin.readline

x,y,w,h = map(int, input().split())

a = x-0
b = y-0
c = w-x
d = h-y

result = min(a,b,c,d)
print(result)
