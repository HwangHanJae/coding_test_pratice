import sys

input = sys.stdin.readline

n = int(input())
line = 0
index = 0
while n > index:
    line+=1
    index += line
diff = index-n
if line % 2==0:
    top = line-diff
    bottom = diff+1
else:
    top = diff+1
    bottom = line-diff

print("{}/{}".format(top, bottom))