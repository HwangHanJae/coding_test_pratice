import sys

n, m = map(int, sys.stdin.readline().split())
words = {}
for _ in range(n):
  word = sys.stdin.readline().rstrip()
  if len(word) < m:
    continue
  if word not in words:
    words[word] = words.get(word, 0) + 1
  else:
    words[word] += 1

words = sorted(words.items(),key=lambda x : (-x[1], -len(x[0]), x[0]))

for word, count in words:
  print(word)