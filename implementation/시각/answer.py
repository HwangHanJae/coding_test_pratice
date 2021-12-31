#n을 입력받는다 
n = int(input())

h = n
m = 60
s = 60
count = 0

for i in range(h+1):
  for j in range(m):
    for k in range(s):
      if "3" in str(i) + str(j) + str(k):
        count+=1

print(count)

#숫자를 문자로 변경해서 하나하나 탐색하는 방법을 기억!
