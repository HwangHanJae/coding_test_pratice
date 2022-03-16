import sys
input =sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

end = 0
sum_value = 0
result = []
for start in range(n):
  while end < n and sum_value < m:
    sum_value += data[end]
    end +=1
  if sum_value >= m:
    result.append(end-start)
  sum_value -= data[start]

if result == []:
  print(0)
else:
  print(min(result))