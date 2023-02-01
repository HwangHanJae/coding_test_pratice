def solution(dartResult):   
    dartResult = dartResult.replace('10', 'n')
    SDT = {"S" : 1, "D" : 2, "T" : 3}
    score = []
    for c in dartResult:
        if c.isdigit() or c == 'n':
            if c == 'n':
                score.append(10)
            else:
                score.append(int(c))
        elif c in SDT:
            c_score = score.pop()
            c_score = c_score ** SDT[c]
            score.append(c_score)
        elif c == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif c =='#':
            score[-1] *= (-1) 
    return sum(score)