from itertools import combinations
n,m = map(int, input().split())

# result = []
# k = 1
# def solve(k):
#   if len(result) == m:
#     print(' '.join(map(str, result)))
#     return
#   for i in range(k, n+1):
#     if i not in result:
#       result.append(i)
#       solve(i+1)
#       result.pop()
    
# solve(k)

array = [i for i in range(1, n+1)]
for lst in combinations(array, m):
  print(' '.join(map(str, lst)))