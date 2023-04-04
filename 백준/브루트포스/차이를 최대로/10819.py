from itertools import permutations

n = int(input())
array = list(map(int, input().split()))


max_num = 0
for A in permutations(array, n):
    sum_value = 0
    for i in range(1, n):
        sum_value += abs(A[i]-A[i-1])
    max_num = max(max_num, sum_value)
print(max_num)