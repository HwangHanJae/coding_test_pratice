def solution(s):
    result = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                result.append(len(sub))
    return max(result)
