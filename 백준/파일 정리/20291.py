n = int(input())
dic = {}
for _ in range(n):
    data = str(input())
    word = data.split('.')[1]
    dic[word] = dic.get(word, 0) + 1

for name, value in sorted(dic.items(), key=lambda x: x[0]):
    print(name, value)