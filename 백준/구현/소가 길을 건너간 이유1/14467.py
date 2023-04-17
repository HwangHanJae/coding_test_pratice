n = int(input())
result = 0
dic = {}
for _ in range(n):
    cow, p = map(int, input().split())
    if cow in dic:
      if dic[cow] == 0 and p == 1:
        dic[cow] = p
        result +=1
      elif dic[cow] == 1 and p == 0:
        dic[cow] = p
        result += 1
    else:
      dic[cow] = p
print(result)
