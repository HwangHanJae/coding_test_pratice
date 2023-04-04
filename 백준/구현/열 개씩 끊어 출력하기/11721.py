word = input()
n = len(word) // 10
for i in range(n+1):
    c = i * 10
    n = (i+1) * 10
    print(word[c:n])
