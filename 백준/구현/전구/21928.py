N, M = map(int, input().split())
array = list(map(int,input().split()))
for _ in range(M):
    a, b, c = map(int,input().split())
    if a == 1:
        array[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if array[i]:
                array[i] = 0
            else:
                array[i] = 1
    elif a == 3:
        for i in range(b-1, c):
            array[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            array[i] = 1
print(' '.join(map(str, array)))