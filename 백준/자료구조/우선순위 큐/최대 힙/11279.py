import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())
for _ in range(n):
    data = int(input())
    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
    #힙은 앞의 있는 값을 기준으로 정렬을 수행하기 때문에 음수를 주어 작게 만들어줌
    #배열은 자동적으로 내림차순으로 될 것임
        heapq.heappush(heap, (-data, data))
   
    