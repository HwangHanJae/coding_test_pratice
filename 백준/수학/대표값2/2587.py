import sys

input = sys.stdin.readline
array = []
for _ in range(5):
  a = int(input())
  array.append(a)

print(int(sum(array) / 5))
print(sorted(array)[2])