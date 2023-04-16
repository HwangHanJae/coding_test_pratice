t = int(input())
for _ in range(t):
    t1, t2 = input().split()
    t1, t2 = int(t1, 2), int(t2, 2)
    result =t1+t2
    print(bin(result)[2:])