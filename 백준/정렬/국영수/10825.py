import sys

input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = map(str, input().split())
    students.append((name, int(kor), int(eng), int(math)))

students = sorted(students, key = lambda x : (-x[1],x[2],-x[3],x[0]))

for i in range(len(students)):
    print(students[i][0])