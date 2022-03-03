import sys
input = sys.stdin.readline

n = int(input())

i = 1
result = 0
while True:
    result += i
    if result > n:
        break
    i+=1
print(i-1)