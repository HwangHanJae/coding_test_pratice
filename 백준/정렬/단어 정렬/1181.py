import sys



n = int(sys.stdin.readline())
words = set()
for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.add(word)

words = sorted(list(words), key=lambda x : len(x))
results = []
for word in words:
    word_len = len(word)
    results.append((word, word_len))
results = sorted(results, key=lambda x : (x[1], x[0]))
for result,_ in results:
    print(result)