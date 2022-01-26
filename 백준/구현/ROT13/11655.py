#a = 97 z = 122
#A = 65 Z = 90

import sys
input = sys.stdin.readline

s = input()
result = ''
for word in s:
    for i in range(len(word)):
        if word[i].isalpha():
            value = ord(word[i]) + 13
            if word[i].isupper():
                if value > 90:
                    value = (value - 90) + 64
                result += chr(value)
            elif word[i].islower():
                if value > 122:
                    value = (value - 122) + 96
                result += chr(value)
        elif word[i].isspace():
            result += ' '
        elif word[i].isalnum():
            result += word[i]


print(result)