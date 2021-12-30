#n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#n개의 개수를 공백으로 구분하여 입력받기
data= list(map(int, input().split()))


import time
start_time = time.time()

#입력받은 수를 정렬하기
data.sort()
first = data[n-1] #가장 큰수
second =data[n-2] #두번째로 큰수

result = 0
while True:
  for i in range(k):   #가장 큰수를 k번 더하기
    if m == 0:         #m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1             #더할 때마다 1씩 빼기
  if m == 0:
    break
  result += second     #두 번째로 큰수를 한번 더하기
  m -= 1
print(result)

end_time = time.time()
print("사용시간 : ", end_time-start_time)
