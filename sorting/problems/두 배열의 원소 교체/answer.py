#답안
n, k = map(int, input().split())    #N과 K를 입력받기
a = list(map(int, input().split())) #배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) #배열 B의 모든 원소를 입력받기

a.sort()              #a는 오른차순으로 정렬
b.sort(reverse=True)  #b는 내림차순으로 정렬

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
  #a의 원소가 b의 원소보다 작은 경우
  if a[i] < b[i]:
    #두 원소를 교체
    a[i], b[i] = b[i], a[i]
  else: #a의 원소가 b의 원소보다 클경우
    break
    
print(sum(a))
