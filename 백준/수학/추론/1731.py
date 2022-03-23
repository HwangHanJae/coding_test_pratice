import sys
input =sys.stdin.readline
n = int(input())
array  = []
for _ in range(n):
  a = int(input())
  array.append(a)
def check(array):
  values = []
  value = array[1]-array[0]
  for i in range(1,len(array)):
    values.append(array[i]-array[i-1])
  for i in values:
    if value != i:
      check = False
      break
    check = True
  if check:
    return (array[-1] +  value)
  else:
    value = array[1] // array[0]
    return (array[-1] *  value)
print(check(array))
