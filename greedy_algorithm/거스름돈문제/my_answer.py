n = 1260
count = 0

coin_types = [500, 100, 50, 10]
for coin in coin_types:
  temp = n // coin
  count = count + temp

  n =  n - (coin * temp)

print(count)
