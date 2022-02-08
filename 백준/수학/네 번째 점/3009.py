import sys

input = sys.stdin.readline
point_set = set()
x_list = []
y_list = []
for _ in range(3):
    x,y = map(int, input().split())
    point_set.add((x,y))
    x_list.append(x)
    y_list.append(y)
    for point_x in x_list:
        for point_y in y_list:
            if (point_x, point_y) not in point_set:
                result_x = point_x
                result_y = point_y
print(result_x, result_y)


