import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))

house = sorted(house)

if n % 2 == 0:
    mid = (n // 2)-1
else:
    mid = int(n/2)

print(house[mid])