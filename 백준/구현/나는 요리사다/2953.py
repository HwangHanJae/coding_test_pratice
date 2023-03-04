winner = (0,0)
for i in range(1, 6):
  score = sum(list(map(int, input().split())))
  if winner[1] < score:
    winner = (i, score)
print(' '.join(map(str, winner)))