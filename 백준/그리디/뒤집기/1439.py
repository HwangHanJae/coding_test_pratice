import sys

input = sys.stdin.readline
s = input().rstrip()

zero = 0
one = 0

for i in range(len(s)-1):
    if s[i] != s[i+1] and  s[i] == "0":
        zero += 1
    elif s[i] != s[i+1] and s[i] == "1":
        one +=1

print(max(zero, one))
