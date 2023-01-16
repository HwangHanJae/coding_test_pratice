def solution(n):
    result = 0
    while n:
        if n % 2 != 0:
            result +=1
            n -= 1
        else:
            n = n//2
    
    return result
        