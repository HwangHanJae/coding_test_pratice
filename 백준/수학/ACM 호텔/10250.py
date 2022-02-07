import sys

input = sys.stdin.readline

def hotel(h,w,n):
    matrix = [[0 for _ in range(h+1)]for _ in range(w+1)]
    count = 1
    for i in range(1,w+1):
        for j in range(1,h+1):
            matrix[i][j] += count
            if matrix[i][j] == n:
                return j, i
            count+=1 



t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor, number = hotel(h,w,n)
    if 1<=number<=9:
        print(str(floor)+"0"+str(number))
    else:
        print(str(floor)+str(number))