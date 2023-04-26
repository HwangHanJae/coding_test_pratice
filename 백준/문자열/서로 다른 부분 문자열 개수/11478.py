s = input()
result = set()
for i in range(len(s)):
    for j in range(len(s)):
        word = s[i:j+1]
        if  word != '':
            print(word)
            result.add(word)
print(len(result))