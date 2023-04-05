def solution(n):
    result = ''
    while n > 0:
        if n % 3 == 0:
            result += '4'
            n  = n // 3 -1
        else:
            result += str(n % 3)
            n //= 3
    return result[::-1]