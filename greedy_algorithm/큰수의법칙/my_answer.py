#큰수의 법칙
#입력파트
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
import time
start_time = time.time()
data.sort() #데이터 정렬

i = 0
result = 0

while i <= m-1:
  result = result + data[n-1] * 1     #첫번째 인덱스의 값을 1번 더해준다.
  i += 1                            #i의 개수를 올려줌
  if i % k == 0:                    #만약 i나누기 k를 했을때 나머지가 0이라면 k의 배수라는 뜻 
    result = result + data[n-2] * 1   #두번째 인덱스를 한번 더해줌
    i += 1                          #i를 개수 올려줌

print(result)

end_time = time.time()
print("사용시간 : ", end_time-start_time)
