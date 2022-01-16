f = [0] * 90
f[0] = 0
f[1] = 1
f[2] = 1
def fibo(x):
    if x == 0:
        return f[x]
    elif x == 1:
        return f[x]
    elif f[x] != 0:
        return f[x]
    else:
        f[x] = fibo(x-2)+fibo(x-1)
        return f[x]


n= int(input())
print(fibo(n))