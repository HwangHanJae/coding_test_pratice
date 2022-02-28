import sys
import heapq
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    q = []
    for _ in range(n):
        name, value = map(str, input().split())
        heapq.heappush(q,(-int(value), name))
    print(q[0][1])