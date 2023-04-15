N = int(input())
array = [i+1 for i in range(N)]
while len(array) > 1:
    temp = []
    for i in range(len(array)):
        #짝수번째 칸
        if (i+1) % 2 == 0:
            temp.append(array[i])
    array =temp.copy()
print(array[0])