N = int(input())
A = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
dic = {}
results = []
for i in A:
  dic[i] = True
for number in numbers:
  if dic.get(number):
    results.append(1)
  else:
    results.append(0)

for result in results:
  print(result)
