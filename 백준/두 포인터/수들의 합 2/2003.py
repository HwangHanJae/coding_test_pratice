import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))

count = 0
sum_value = 0
end = 0

for start in range(n):
  while end < n and sum_value < m:
    sum_value += array[end]
    end+=1
  if sum_value == m:
    count += 1
  sum_value -= array[start]
print(count)