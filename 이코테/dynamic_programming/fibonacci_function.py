#피보나치 함수를 재귀함수로 구현
import time
# def fibo(n):
#   if n==1 or n==2:
#     return 1
#   return fibo(n-1)+fibo(n-2)

# start_time = time.time()
# print(fibo(30))
# end_time = time.time()

# print("시간 : ",end_time-start_time)

#n의 값이 늘어날 수록 계산 시간은 늘어남

#다이나믹프로그래밍의 조건
# 1.큰 문제를 작은 문제로 나눌 수 있다.
# 2.작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

#메모이제이션 기법을 사용해서 구현
#: 한번구한 결과를 메모리 공간에 메모해두고 같은 식으로
#: 다시 호출하면 메모한 결과를 그대로 가져오는 기법
#메모이제이션은 값을 저장하는 방법으로 캐싱이라고 한다.

#한번 계산된 결과를 메모이 제이션하기 위한 리스트 초기화
d = [0] * 100

#재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo_topdown(x):
  #종료 조건
  if x == 1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
  return d[x]
start_time = time.time()
print(fibo_topdown(30))
end_time = time.time()

print("시간 : ",end_time-start_time)

print("시간이 짧아진것을 확인할 수 있다.")

#호출되는 함수 확인(탑다운)
d = [0] * 100
def pibo(x):
  print('f('+str(x)+')', end=' ')
  if x==1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pibo(x-1) + pibo(x-2)
  return d[x]

pibo(6)

#피보나치 수열(반복문)
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1

n = 99
for i in range(3, n+1):
  d[i] = d[i-1]+d[i-2]

print() 
print(d[30])
