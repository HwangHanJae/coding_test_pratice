#재귀함수(Recursive Function)
#자기 자신을 다시 호출하는 함수
def recursive_fuc():
  print("재귀 함수를 호출합니다.")
  recursive_fuc()

#recursive_fuc()

#재귀함수는 무한 호출되기 때문에 반드시 '종료조건'을 명시해야 한다.

#재귀함수를 100번 호출하도록 작성한 함수
def recursive_fuction(i):
  #100번쨰 출력했을 때 종료되도록 종료 조건 명시
  if i == 100:
    return
  print(i, "번째 재귀 함수에서", i+ 1,"번째 재귀 함수를 호출합니다.")
  recursive_fuction(i+1)
  print(i, "번째 재귀 함수를 종료합니다.")

recursive_fuction(1)
