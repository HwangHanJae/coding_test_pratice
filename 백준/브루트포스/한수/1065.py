n = int(input())
def check(j):
    array = list(map(int, str(j)))
    count = 1
    #1000보다 작은수이기 때문에 3자리가 최대 자리이다.
    #1번의 검사만 진행한다.
    for i in range(len(array) - 2):
        #가장 끝자리와 중간자리를 더한값과 중간자리에서 가장 첫 자리를 뺀 값이 같지 않다면
        if array[i+2] - array[i+1] != array[i+1] - array[i]:
            count = 0
            break
        else :
            count = 1
    #위의 과정을 거치고 count=1이나오면 등차 수열임을 확인 할 수 있다.
    return count
count = 0
total = 0
for i in range(1, n+1):
    count = check(i)
    total += count

print(total)