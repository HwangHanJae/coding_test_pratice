import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1, y1, r1, x2,y2,r2 = map(int, input().split())

    d = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
    # 두원의 중심위치가 같을 때
    if d == 0:
        # 반지름이 같다면 두 개의 원은 겹친다는 것
        if r1 == r2:
            print(-1)
        else:
            print(0)
    #두 원의 중심위치가 서로 다를 때
    else:
        #원의 중심 사이 거리가 각각의 반지름의 합과 차이와 같다면
        if d == (r1+r2) or d == abs(r1-r2):
            print(1)
        # 원의 중심 사이의 거리보다 반지름이 합이 더 크고, 반지름의 차가 더 작으면
        elif d < (r1+r2) and d > abs(r1-r2):
            print(2)
        else:
            print(0)