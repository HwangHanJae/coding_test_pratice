import math
def solution(n, k):
    result = 0
    k_number = k_change(n, k)
    numbers = k_number.split('0')
    for number in numbers:
        if number == '':
            pass
        else:
            if is_prime(int(number)):
                result +=1
    return result

def k_change(n, k):
    result = ''
    while n:
        result += str(n % k)
        n = n // k
    return result[::-1]

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) +1 ):
        if number % i == 0:
            return False
    return True
            
    