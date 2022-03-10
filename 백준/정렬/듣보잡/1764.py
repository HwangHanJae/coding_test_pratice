import sys

input =sys.stdin.readline
n, m = map(int, input().split())

n_names = []
m_names = []

for _ in range(n):
  n_names.append(input().rstrip())
for _ in range(m):
  m_names.append(input().rstrip())

n_names.sort()
n_dic = {}
m_dic = {}
for i in n_names:
  n_dic[i] = 1
for i in m_names:
  try:
    n_dic[i] += 1
  except:
    pass
  
result = []
for i in n_dic:
  if n_dic[i] == 2:
    result.append(i)
print(len(result))
for i in result:
  print(i)
