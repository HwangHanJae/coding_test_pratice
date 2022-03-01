import sys
input = sys.stdin.readline


data = input().rstrip()
or_s = []
re_s = []
for i in range(len(data)):
    or_s.append(data[i])
for i in range(len(data)-1, -1, -1):
    re_s.append(data[i])

check_count=0
for i in range(len(data)//2):
    if or_s[i] == re_s[i]:
        check_count+=1
    else:
        check_count-=1

if check_count == len(data)//2:
    print(1)
else:
    print(0)


