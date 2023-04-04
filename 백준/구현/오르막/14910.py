A = list(map(int, input().split()))
if len(A) == 1:
    print('Good')
else:    
  for i in range(len(A)-1):
      if A[i]<= A[i+1]:
          pass
      else:
          print('Bad')
          break
  else:
      print('Good')