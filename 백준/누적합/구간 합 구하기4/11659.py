import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
sum_values = [0]

sum_value = 0
for i in data:
  sum_value += i
  sum_values.append(sum_value)

for _  in range(m):
  left, right = map(int, input().split())
  result = sum_values[right] - sum_values[left-1]
  print(result)