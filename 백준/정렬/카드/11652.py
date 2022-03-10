import sys

input = sys.stdin.readline

array =[]
n = int(input())
for _ in range(n):
  data = int(input())
  array.append(data)

dic = {}
for i in range(len(array)):
  if array[i] in dic:
    dic[array[i]] += 1
  else:
    dic[array[i]] = 1


dic = sorted(dic.items(), key= lambda x : (-x[1], x[0]))


print(dic[0][0])
