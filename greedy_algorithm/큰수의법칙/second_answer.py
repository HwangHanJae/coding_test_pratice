#두번째 답
#n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())
#data를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

import time
start_time = time.time()

#data 정렬하기
data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m-count) * second
print(result)

end_time = time.time()
print("사용시간 : ", end_time-start_time)
