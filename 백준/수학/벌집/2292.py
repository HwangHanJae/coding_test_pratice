import sys

input = sys.stdin.readline

n = int(input().rstrip())

start = 2
end = 7
diff = 6
num = 2
while True:
    if n == 1:
        print(1)
        break
    if start <= n <= end:
        print(num)
        break
    else:
        start += diff
        diff += 6
        end = end + diff
        num += 1
