import sys
input = sys.stdin.readline
for i in range(int(input())):
  result = input().rstrip()
  print("{}. {}".format(i+1, result))