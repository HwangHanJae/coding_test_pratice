import sys
input =sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
t = int(input())
sum_value = 0
array = [0]
for i in range(n):
  sum_value +=data[i]
  array.append(sum_value)

for _ in range(t):
  s, e = map(int,input().split())
  print(array[e]-array[s-1])