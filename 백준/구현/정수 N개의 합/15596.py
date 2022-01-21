def solve(a):
    ans = 0
    for i in range(len(a+1)):
        ans += a[i]
    return ans