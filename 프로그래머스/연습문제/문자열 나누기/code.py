def solution(s):
    result = 0
    #x와 같은 글자의 수
    count1 = 0
    #x와 다른 글자의 수
    count2 = 0
    for i in range(len(s)):
        if count1 == count2:
            result += 1
            x = s[i]
        if s[i] == x:
            count1 +=1
        else:
            count2 += 1

    return result
