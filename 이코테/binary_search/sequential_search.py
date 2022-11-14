#순차 탐색
#: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
#기본 탐색 방법 

#문제 풀이
n, s = input().split()

s_list = input().split()
result = 0
for i in range(len(s_list)):
  if s_list[i] == s:
    result = i+1
print(result)


#답
#순차 탐색 소스코드 구현
def sequential_search(n, target, array):
  #각 원소 하나씩 확인하며
  for i in range(n):
    if array[i] == target:
      return i +1 #현재의 위치 반환(인덱스는 0부터 시작하여 1 더하기)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) #원소의 개수
target = input_data[1] #찾고자 하는 문자열을

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")

array = input().split()


print(sequential_search(n, target, array))
