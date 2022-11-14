import time
n = int(input())

문제 풀이
def check(n):
  count = 0
  n = n-1
  count+=1
  while n != 1:
    if n % 5 ==0:
      n = n/5
      count+=1
    elif n % 3 == 0:
      n = n/3
      count+=1
    elif n %2 == 0:
      n = n/2
      count+=1
  return count

start_time = time.time()

print(check(n))
end_time = time.time()

print("시간 : ", end_time - start_time)
