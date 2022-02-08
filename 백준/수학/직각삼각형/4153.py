import sys

input = sys.stdin.readline

def check(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2+c**2==a**2:
        return True
    else:
        return False


while True:
    a,b,c = map(int, input().split())
    if (a,b,c)==(0,0,0):
        break
    if check(a,b,c):
        print("right")
    else:
        print("wrong")
