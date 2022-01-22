n = int(input())
count = n
for _ in range(n):
    data = input()
    for i in range(len(data)-1):
        #전체 단어를 돌면서 현재단어와 다음 단어가 같다면 넘어간다.
        if data[i] == data[i+1]:
            pass
        #현재 단어와 다음단어가 같지 않은데, 다음 단어들 중에 현재 단어가 있다면
        #전체 개수에서 카운트를 빼고 반복문을 탈출하고 다음 data를 확인
        elif data[i] in data[i+1:]:
            count -= 1
            break
print(count)
