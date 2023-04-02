N = int(input())
B = list(map(int, input().split()))
A = [-1 for _ in range(N)]
for i in range(N):
  A[i] = (B[i] * (i+1)) - sum(A[:i])
print(' '.join(list(map(str, A))))