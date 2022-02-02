import sys


d = [[0,0] for _ in range(40+1)]
d[0] = [1,0]
d[1] = [0,1]
for i in range(2, 40+1):
    d[i][0] = d[i-1][0]+d[i-2][0]
    d[i][1] = d[i-1][1]+d[i-2][1]

input = sys.stdin.readline 
n = int(input())
for _ in range(n):
    case = int(input())
    zero = d[case][0]
    one = d[case][1]
    print(zero, one)
    