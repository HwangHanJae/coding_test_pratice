import sys
import heapq
input =sys.stdin.readline
matrix =[]
result = []
for _ in range(9):
  matrix.append(list(map(int, input().split())))
value = 0
for i in range(9):
  for j in range(9):
    heapq.heappush(result,(-matrix[i][j],i+1,j+1))

print(-1 * result[0][0])
print(result[0][1], result[0][2])