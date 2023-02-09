def solution(n):
    num = 1000000007
    d = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
        d[i] = d[i] % num
    return d[n]