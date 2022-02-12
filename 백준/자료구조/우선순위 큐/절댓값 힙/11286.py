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
            pop = heapq.heappop(heap)[1]
            print(pop)
    else:
        heapq.heappush(heap, (abs(data), data))