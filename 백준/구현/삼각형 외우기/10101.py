a = int(input())
b = int(input())
c = int(input())
# 세 각의 크기가 모두 60인 경우
if a == 60 and b == 60 and c == 60:
    print("Equilateral")
# 세 각의 합이 180인 경우
elif a+b+c == 180:
    dic = {}
    for i in [a,b,c]:
        dic[i] = dic.get(i, 0) + 1
    for i in [a,b,c]:
        # 두 각의 같은 경우
        if dic[i] == 2:
            print("Isosceles")
            break
    # 같은 각이 없는 경우
    else:
        print('Scalene')
# 세 각의 합이 180이 아닌 경우
else:
    print("Error")