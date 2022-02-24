import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))
result = 0
value = 0
while q:
    if len(q) == 1:
        result += heapq.heappop(q)
        break
    if len(q) != 2:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        sum = a+b
        result += sum
        heapq.heappush(q, sum)
    else:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        sum = a+b
        result += sum
if n == 1:
    print(0)
else:
    print(result)