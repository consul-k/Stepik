def calculate_average_age(employees):
    total_age = 0
    count = 0

    for employee in employees:
        if 'age' in employee:
            total_age += employee['age']
            count += 1

    if count == 0:
        return 0

    average_age = total_age / count
    return average_age

average_age = calculate_average_age(employees)
print(average_age)
