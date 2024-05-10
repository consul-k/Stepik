# вводные данные              
disease = {
    1: 'хворь', 2: 'бобока',
    3: 'скитлстрянка', 4: 'перелом сознания',
    5: 'шерстевыделение', 6: 'газированные слезы'
}

# продолжите решение здесь
a = set(map(int, input().split()))
b = set(map(int, input().split()))
status = a-b
remaining_diseases = ', '.join(disease.get(i) for i in status)
if not status:
    print('Пациент здоров')
else:
    print(f'Пациент еще болен: {remaining_diseases}')
