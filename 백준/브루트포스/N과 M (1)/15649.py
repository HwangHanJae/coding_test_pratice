from itertools import permutations
n, m = map(int, input().split())
array = [i for i in range(1, n+1)]
result = []

for lst in permutations(array, m):
  print(' '.join(map(str, lst)))