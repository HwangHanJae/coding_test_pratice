#큐 예제
#큐를 구현하기 위해는 deque 라이브러리 사용
from collections import deque
queue = deque()

queue.append(5) #5 삽입 5
queue.append(2) #2 삽입 2-5
queue.append(3) #3 삽입 3-2-5
queue.append(7) #7 삽입 7-3-2-5
queue.popleft() #삭제(5가 삭제)  7-3-2
queue.append(1) #1 삽입 1-7-3-2
queue.append(4) #4 삽입 4-1-7-3-2
queue.popleft() #삭제(2가 삭제) 4-1-7-3

#출력
print(queue) #먼저 들어온 순서대로 출력

#다음 출력을 위해 역순으로 바꾸기
queue.reverse()
print(queue) #나중에 들어온 순서대로 출력
