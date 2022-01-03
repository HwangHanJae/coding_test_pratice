#재귀함수를 구현한는 대표적 예제
#반복적으로 구현한 n!

def factorial(n):
  result = 1
  #1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result *= i
  return result



def factorial_recursive(n):
  if n<=1:
    return 1
  #n! = n * (n-1)!을 그대로 코드로 작성하기
  return n * factorial_recursive(n-1)

num = 5
print("반복적으로 구현한 예 : ",factorial(num))
print("재귀적으로 구현한 예 : ",factorial_recursive(num))
