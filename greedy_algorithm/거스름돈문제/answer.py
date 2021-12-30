#그리디 알고리즘
#거스름돈 대표적 문제
n = 1260
count = 0

#큰 단위 화폐부터 차례로 확인
coin_types =[500, 100, 50, 10]

for coin in coin_types:
    #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  temp = n // coin     # 거스름돈과 coin을 나누어서 몫을 계산함
  count = count + temp # 몫과 count 더 해줌
 
  n = n%coin           # 위에서 몫 만큼 coin을 거슬러주었으니 나머지 거스름돈을 계산하고 변수에 할당 
  
print(count)
