def cal_T():
  n = 1
  array = []
  while True:
    number = int(n * (n+1) / 2)
    if number > 1000:
      break
    array.append(number)
    n+=1
  return array
def ureka(k, T):
  for i in range(len(T)):
    for j in range(len(T)):
      for n in range(len(T)):
        if (T[i] + T[j] + T[n]) == k:
          return 1
  return 0

T = cal_T()
for _ in range(int(input())):
  k = int(input())
  print(ureka(k, T))