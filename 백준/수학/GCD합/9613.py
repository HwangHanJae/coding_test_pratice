import math
import sys

n = int(sys.stdin.readline())


for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    t = data[0]
    result = 0
    for i in range(1, t):
        for j in range(i+1, t+1):
            if i == j or i > j:
                pass
            else:
                result += math.gcd(data[i], data[j])
    print(result)