list_grade = list(map(int, input().split()))
result_average = round(sum(list_grade) / len(list_grade))
print(f'Оценка за четверть: {result_average}')
