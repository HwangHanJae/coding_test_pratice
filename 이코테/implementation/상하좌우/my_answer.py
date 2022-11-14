import time
#공간의 크기를 나타내는 n
n = int(input())
#n = 5
move = list(map(str, input().split()))
#move = ["R", "R", "R", "U", "D", "D"]

start_time = time.time()
#시작위치를 지정
start_point_front, start_point_back = 1,1
#현재위치를 시작 위치로 지정
current_point_front, current_point_back = start_point_front, start_point_back

#조건에 해당하는 값들을 확인
for con in move:
  #현재위치가 시작위치이기 때문에 좌, 상으로 이동할 수 없는경우
  if current_point_back == start_point_back and con == "L":
      current_point_back += 0
  elif current_point_front == start_point_front and con == "U":
      current_point_front += 0      
  #현재위치가 마지막위치이기 때문에 우, 하으로 이동할 수 없는경우
  elif current_point_back == n and con == "R":
    current_point_back += 0
  elif current_point_front == n and con == "D":
    current_point_front += 0
  #위의 조건이 아닌경우에 현재 위치에 값을 더해주고 이동수행
  elif con == "R":
    current_point_back +=1
  elif con == "L":
    current_point_back -=1
  elif con == "U":
    current_point_front -=1
  elif con == "D":
    current_point_front +=1

print(current_point_front, current_point_back)

end_time = time.time()
print("시간 체크 : ",end_time - start_time)
