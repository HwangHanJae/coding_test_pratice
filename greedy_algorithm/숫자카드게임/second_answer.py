#2중 반복문을 이용한 답
n, m = map(int, input().split())

result = 0
#한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  #현재 줄 에서 '가장 작은 수' 찾기
  min_value = 10001
  for j in data:
    min_value = min(min_value, j)
  #'가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)
print(result)
