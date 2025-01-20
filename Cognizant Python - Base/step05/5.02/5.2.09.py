anna_grades = input()
boris_grades = input()
victoria_grades = input()

anna_grades = list(map(int, anna_grades.split()))
boris_grades = list(map(int, boris_grades.split()))
victoria_grades = list(map(int, victoria_grades.split()))

# Добавляем новые оценки в словарь
students["Анна"]["математика"].append(anna_grades[0])
students["Анна"]["физика"].append(anna_grades[1])
students["Анна"]["химия"].append(anna_grades[2])

students["Борис"]["математика"].append(boris_grades[0])
students["Борис"]["физика"].append(boris_grades[1])
students["Борис"]["химия"].append(boris_grades[2])

students["Виктория"]["математика"].append(victoria_grades[0])
students["Виктория"]["физика"].append(victoria_grades[1])
students["Виктория"]["химия"].append(victoria_grades[2])

# Выводим изменённый словарь
print(students)
