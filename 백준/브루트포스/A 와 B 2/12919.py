S = list(input())
T = list(input())
def backtracking(now):
  global flag
  if now == S:
    flag = True
  
  if len(now) > 1:
    if now[-1] =='A':
      backtracking(now[:-1])
    if now[0] == 'B':
      backtracking(now[::-1][:-1])

flag = False  
backtracking(T)
if flag:
  print(1)
else:
  print(0)