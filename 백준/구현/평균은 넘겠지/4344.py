c = int(input())
for _ in range(c):
    array = list(map(int, input().split()))
    n = array[0]
    mean = (sum(array)- array[0]) / (len(array) - 1)
    count = 0
    for i in range(1, len(array)):
        if array[i] > mean:
            count += 1
    value = count / (len(array) - 1)
    result = value*100
    print("{:.3f}%".format(result))