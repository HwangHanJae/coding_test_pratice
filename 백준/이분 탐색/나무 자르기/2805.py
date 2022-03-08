import sys

input = sys.stdin.readline


def total_solve(n, mid):
  total = 0
  for i in range(n):
    if array[i] >= mid:
      total += (array[i] - mid)
  return total
  
n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

while start <= end:
  total = 0
  mid = (start + end)//2
  total = total_solve(n, mid)
  if total >= m:
    start = mid+1
    result = mid
  else :
    end = mid-1
print(result)
