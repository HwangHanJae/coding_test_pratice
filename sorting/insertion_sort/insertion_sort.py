#삽입정렬(Insertion Sort)
#데이터가 '거의 정렬' 되어 있을 때 효율적
#데이터가 적절한 위치를 찾고 삽입을 한다.
#삽입을 할때 자신보다 작은 값을 만나면 그 자리에 삽입을 한다 이유는 자신보다 작은 값 앞에 있는 데이터는 이미 정렬이 되어있다고 판단하기 때문

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
  for j in range(i, 0, -1): #인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j-1]: #한칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j] 
    else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)

#시간복잡도는 O(N²) 정렬이 되어 있는 상태면(최선의 상태) O(N)
