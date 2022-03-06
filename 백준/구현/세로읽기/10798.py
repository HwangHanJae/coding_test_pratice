import sys

input = sys.stdin.readline

array = [[]for _ in range(15)]
for _ in range(5):
  words = input().rstrip()
  for i, word in enumerate(words):
    array[i].append(word)
result = ''
for i in range(len(array)):
  result += ''.join(array[i])
print(result)