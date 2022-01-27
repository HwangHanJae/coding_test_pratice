n = int(input())
def fibo(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibo(n-1) + fibo(n-2)
        return result
print(fibo(n))