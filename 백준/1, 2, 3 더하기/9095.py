def f(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else :
        return f(n-1)+f(n-2)+f(n-3)

data = int(input())

for _ in range(data):
    n = int(input())
    print(f(n))