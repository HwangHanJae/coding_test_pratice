#집합 자료형을 이용하여 풀기
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print("yes", end=' ')
  else:
    print("no", end=' ')
