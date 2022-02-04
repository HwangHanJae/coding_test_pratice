import sys

input = sys.stdin.readline

s = input().rstrip()
n = int(len(s) / 2)
front = 0
front_s = s[:n]
back = 0
back_s = s[n:]
for i in range(len(front_s)):
    front += int(front_s[i])

for i in range(len(back_s)):
    back += int(back_s[i])

if front == back:
    print("LUCKY")
else:
    print("READY")