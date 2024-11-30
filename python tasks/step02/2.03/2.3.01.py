n = int(input())

students = {}

for _ in range(n):
    data = input().split()
    surname = data[0]
    grade = int(data[1])
    students[surname] = grade

query_surname = input()

if query_surname in students:
    print(students[query_surname])
else:
    print(f"Ученик с фамилией {query_surname} не найден.")
