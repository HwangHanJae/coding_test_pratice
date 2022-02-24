import sys

input = sys.stdin.readline

matrix = []

n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = matrix[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = matrix[i-1][j]
        matrix[i][j] = matrix[i][j] + max(up_left, up)
print(max(matrix[n-1]))
        