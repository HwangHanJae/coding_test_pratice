n, k = map(int,input().split())

a = input().split()
b = input().split()

def type_change(array):
  for i in range(len(array)):
    array[i]= int(array[i])
  return array

a = type_change(a)
b = type_change(b)

#a는 오름차순으로 바꾸기
a=sorted(a, reverse=False)

#b는 내림차순으로 바꾸기
b = sorted(b, reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
