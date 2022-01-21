n = int(input())

for i in range(n):
    count = 0                   #"O"가 몇번 연속되는지 확인하는 변수
    result = 0                  #최종 결과를 담을 변수
    o_x = input()
    for j in range(len(o_x)):   
        if o_x[j] == "O":       #O가 나올때마다
            count  +=1          #count의 개수를 늘려주고
            result += count     #count의 개수를 result에 저장한다/.
        else:                   #"X"가 나올때마다
            count = 0           # count를 0으로 초기화 시켜준다.
    print(result)