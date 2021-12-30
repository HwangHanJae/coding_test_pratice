#숫자 카드 게임
#n은 행, m은 열
#입력
n,m = map(int, input().split())

number = []
for row in range(n):
  row_list = list(map(int, input().split()))
  row_list.sort()
  for i in row_list:
    number.append(row_list[0])
    break
number.sort()
result = number[n-1]
print(result)
