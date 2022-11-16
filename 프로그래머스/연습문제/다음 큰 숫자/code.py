def solution(n):
    number = (n+1)
    print(type(bin(n)[2:]))
    while True:
        b_n = list(map(int, bin(n)[2:]))
        b_number = list(map(int, bin(number)[2:]))
        if sum(b_n) == sum(b_number):
            return number
        else:
            number += 1