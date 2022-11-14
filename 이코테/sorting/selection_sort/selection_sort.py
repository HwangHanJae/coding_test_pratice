#선택정렬(Selection Sort)
#가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 , 그 다음 작은 데이터를 선택해 두 번째데이터와 바꾼다
#매번 가장 작은것을 선택

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
  break#스와프


print(array)

#선택 정렬의 시간 복잡도
#O(N²) : N + (N-1) + (N-2) ... + 2 --> N X N+1 / 2 == (N² + N) / 2

