n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1
for x in data:
    #만들수 없는 금액을 찾았을때 반복 종료
    if target < x:
        break
    target += x

print(target)


