def solution(dots):
    dic = {}
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            x = dots[i][0] - dots[j][0]
            y = dots[i][1] - dots[j][1]
            if x == 0:
                dic[x] = dic.get(x, 0) + 1
            else:
                 dic[y / x] = dic.get(y / x, 0) + 1
    for key in dic:
        if dic[key] > 1:
            return 1
    return 0