import sys
input = sys.stdin.readline


results = ["D","C","B","A",'E']
for _ in range(3):
  array = list(map(int, input().split()))
  print(results[sum(array)])