grades = input().split()

grades = [int(grade) for grade in grades]

highest_grade = grades[0]
count = 0

for grade in grades:
    if grade > highest_grade:
        highest_grade = grade
        count = 1
    elif grade == highest_grade:
        count += 1

print(f"Самая высокая оценка: {highest_grade}")
print(f"Количество: {count} шт")
