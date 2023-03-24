import sys

t =int(sys.stdin.readline().strip())
for _ in range(t):
  numbers = []
  flag = True
  n = int(sys.stdin.readline().strip())

  numbers = [sys.stdin.readline().strip() for _ in range(n)]
  numbers.sort()
  for i in range(n-1):
    front = len(numbers[i])
    if numbers[i] == numbers[i+1][:front]:
      flag = False
      break

  if flag == False:
    print('NO')
  else:
    print('YES')