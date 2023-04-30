X = int(input())
N = int(input())
sum_value = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum_value += (a*b)

if sum_value == X:
    print("Yes")
else:
    print("No")