t = int(input())
d = {}
for i in range(1,30+1):
    for j in range(i,30+1):
        if i == 1:
            d[(i, j)] = i * j
        elif i == j:
            d[(i, j)] = 1
        else:
            d[i, j] = d[(i, j-1)] + d[(i-1, j-1)]
for _ in range(t):
    n, m = map(int, input().split())
    print(d[(n, m)])