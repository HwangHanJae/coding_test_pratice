import sys
import heapq

def heap_sort(array):
    result = []
    heap = []
    for i in range(len(array)):
        heapq.heappush(heap, array[i])
    while heap:
        result.append(heapq.heappop(heap))
    return result
input =sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array = list(set(array))
result = heap_sort(array)
for i in result:
    print(i, end=' ')