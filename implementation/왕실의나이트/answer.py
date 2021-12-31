#답안을 보고 다시 작성한 코드
input_data = input()

import time
start_time = time.time()

texts = ["a","b","c","d","e","f","g","h"]
def text_to_int(string):
  for i, text in enumerate(texts,1):
    if string == text:
      return int(i)

row = int(input_data[1])
col = input_data[0]
col = text_to_int(col)

steps = [(-2,1),(-2,-1),(-1,2),(1,2),(2,1),(2,-1),(-1,-2),(1,-2)]
count =0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  #(1,1)~(8,8)이 최소,최대
  if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    count +=1

print(count)
end_time = time.time()
print("시간 : ",end_time-start_time)
