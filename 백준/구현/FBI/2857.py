result = []
for i in range(1,6):
  name = input()
  if "FBI" in name:
    result.append(str(i))

if result == []:
  print("HE GOT AWAY!")
else:
  print(' '.join(result))