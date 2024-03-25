n = int(input())
grades = []
for _ in range(n):
    grade = int(input())
    if grade != 4 and grade != 5:
        grades.append(grade)
for grade in grades:
    print(grade)
