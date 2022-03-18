import sys
input = sys.stdin.readline

words = input().rstrip()
result = ''
for i in words:
    if i.islower():
        result += i.upper()
    elif i.isupper():
        result += i.lower()
print(result)
