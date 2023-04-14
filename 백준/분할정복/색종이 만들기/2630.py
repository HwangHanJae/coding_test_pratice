N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
zeros = 0
ones = 0
def solve(n,array):
    global zeros
    global ones
    all_zeros = True
    all_ones = True
    if n == 1:
        if array[0][0] == 0:
            zeros += 1
        else:
            ones += 1
        return
    for i in range(0, n):
        for j in range(0, n):
            if array[i][j] != 0:
                all_zeros = False
            if array[i][j] != 1:
                all_ones = False
    if all_zeros:
        zeros += 1
        return
    if all_ones:
        ones += 1
        return
    n = n // 2
    solve(n, [[col for col in row[:n]] for row in array[:n]])
    solve(n, [[col for col in row[:n]] for row in array[n:]])
    solve(n, [[col for col in row[n:]] for row in array[:n]])
    solve(n, [[col for col in row[n:]] for row in array[n:]])

solve(N, array) 
print(zeros)
print(ones)            
