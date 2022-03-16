import sys
input =sys.stdin.readline
n = int(input())

end= 0
sum_value = 0
count = 0
for start in range(1, n+1):
  while end < n and sum_value < n:
    sum_value += end
    
    end+=1
  if sum_value == n:
    count+=1
  sum_value -= start
  
print(count+1)