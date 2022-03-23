import sys
input =sys.stdin.readline

array = []
for _ in range(8):
  array.append(int(input()))
sorted_array = sorted(array, reverse=True)

results = []
for i in range(5):
  results.append(array.index(sorted_array[i])+1)

print(sum(sorted_array[:5]))
for result in sorted(results):
  print(result, end = ' ')