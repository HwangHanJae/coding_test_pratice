import sys
input =sys.stdin.readline

def solve(n):
  result = []
  for i in range(2, n+1):
    j = 1
    while i * j <= n:
      if i * j in result:
        pass
      else:
        result.append(i*j)
      j+=1
  return result

n, k = map(int, input().split())
result =solve(n)
print(result[k-1])