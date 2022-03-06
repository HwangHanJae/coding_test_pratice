import sys

input = sys.stdin.readline

def binary_search(array,start,end,target):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return target
    elif array[mid] > target:
      end = mid-1
    elif array[mid] < target:
      start = mid+1
  return None

array = [i for i in range(1,101)]
result = []
a = int(input())
b = int(input())
for i in range(a, b+1):
  if binary_search(array,0,len(array),i**(0.5)) != None:
    result.append(i)

if len(result) == 0:
  print(-1)
else:
  print(sum(result))
  print(min(result))