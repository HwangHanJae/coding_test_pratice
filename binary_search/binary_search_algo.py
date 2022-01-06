#이진 탐색
#배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘

#시작점, 끝점, 중간점 3개의 변수를 사용
#찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

array = [1,3,5,7,9,11,13,15,17,19]
n = 10
target = 7

#1.재귀함수를 이용한 이진 탐색
def binary_search_recursive(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search_recursive(array, target, start, mid-1)
  else:
    return binary_search_recursive(array, target, mid+1, end)

result = binary_search_recursive(array, target, 0, n-1)

if result == None:
  print("None")
else:
  print(result + 1)

#2.반복문을 이요한 이진 탐색
def binary_search_while(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우
    if array[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  return None

result = binary_search_while(array, target, 0, n-1)

if result == None:
  print("None")
else:
  print(result + 1)
