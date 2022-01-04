#퀵 정렬(Quick Sort) 빠른 정렬 알고리즘
#기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
#기준 == 피벗(Pivot)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    #피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

#파이썬을 활용한 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort_python(array):
  #리스트 하나만 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort_python(left_side)+[pivot]  + quick_sort_python(right_side)

print(quick_sort_python(array))

