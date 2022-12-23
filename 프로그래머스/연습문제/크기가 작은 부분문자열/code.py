def solution(t, p):
    l = len(p)
    result = 0
    for i in range(len(t)):
        word = t[i:i+l]
        print(word)
        if len(word) == l:
            if int(word) <= int(p):
                result += 1
    return result
    