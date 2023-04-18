money = int(input())
array = list(map(int, input().split()))

def J(array, money):
    count = 0
    for i in array:
        d, m = divmod(money, i)
        money = m
        count += d
    return count * array[-1] + money

def S(array, money):
    count = 0
    check = [0 for _ in range(len(array))]
    for i in range(len(array)-3):
        if array[i] < array[i+1] and array[i+1] < array[i+2]:
            check[i+3] = 1
        elif array[i] > array[i+1] and array[i+1] > array[i+2]:
            check[i+3] = -1
        if check[i+3] == 1:
            money += count * array[i+3]
            count = 0
        elif check[i+3] == -1:
            d, m = divmod(money, array[i+3])
            money = m
            count += d
    return count * array[-1] + money

j = J(array, money)
s = S(array, money)
if j > s :
    print("BNP")
elif s > j:
    print("TIMING")
else:
    print("SAMESAME")