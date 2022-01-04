n = int(input())

input_list = []
for i in range(n):
  input_data = list(input().split())
  name, score = input_data[0], input_data[1]
  input_list.append((name, int(score)))

def setting(data):
  return data[1]

input_list = sorted(input_list, key=setting)
for i in range(len(input_list)):
  print(input_list[i][0], end=' ')
