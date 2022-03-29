import sys

input = sys.stdin.readline
array = []
n= 10
dic = {}
for _ in range(n):
  a = int(input())
  dic[a] = 0
  array.append(a)

for i in range(len(array)):
  dic[array[i]] +=1
print(int(sum(array) / n))

for key, value in dic.items():
  if value == max(dic.values()):
    print(key)