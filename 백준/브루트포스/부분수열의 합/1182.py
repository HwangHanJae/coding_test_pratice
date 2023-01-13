from itertools import combinations
n, s = map(int, input().split())
array = list(map(int, input().split()))
result = 0
for i in range(1, n+1):
  for numbers in combinations(array, i):
    if sum(numbers) == s:
      result += 1
print(result)