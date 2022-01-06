문제풀이
n = int(input())
array = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

#순차 탐색
def sequentail_search(array, target):
  for i in range(len(array)):
    if target == array[i]:
      return 'yes'
  return 'no'

result =[]
for i in range(m):
  result.append(sequentail_search(array, target_list[i]))

for i in range(len(result)):
  print(result[i], end=' ')

#이진 탐색
array.sort()
target_list.sort()

def binary_search(array, start, end, target):
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target:
      return 'yes'
    elif array[mid] > target:
      end = mid-1
    else : 
      start = mid +1
  return "no"

result =[]
for i in range(m):
  result.append(binary_search(array, 0, n-1, target_list[i]))

for i in range(len(result)):
  print(result[i], end=' ')
