A, B = map(int,input().split())

count = 0
while True:
  if B < A:
    count = -1
    break
  if A == B:
    break
  if B % 2 == 0:
    B = B // 2
    count += 1
  elif str(B)[-1] == str(1):
    B = int(str(B)[:-1])
    count += 1
  else:
    count = -1
    break

if count == -1:
  print(count)
else:
  print(count+1)

