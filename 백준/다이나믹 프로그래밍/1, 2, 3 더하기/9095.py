#다이나믹 프로그래밍문제로 반복되는 구조를 찾아내고 식으로 구현하는 것이 중요함

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

