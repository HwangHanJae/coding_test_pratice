import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    data = int(input())
    if data > 0:
        heapq.heappush(heap, data)
    else:
        if len(heap) == 0:
            print(0)
        else:
            pop = heapq.heappop(heap)
            print(pop)