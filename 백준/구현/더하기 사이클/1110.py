n = int(input())

count = 0
original = n
while True:
    #10으로 나누었을 때 몫
    a = n // 10
    #10으로 나누었을 때 나머지
    b = n % 10
    #위의 두 값을 더하고 10을 나누어서 1의 자리를 구함
    value = (a + b) % 10
    new_number = (10 * b) + value
    count+=1
    if new_number == original:
        break
    n = new_number

print(count)