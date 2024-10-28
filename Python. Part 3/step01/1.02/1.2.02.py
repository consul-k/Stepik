filtered_employees = []
for employee in employees:
    if employee['age'] < 35:
        filtered_employees.append(employee)

print(filtered_employees)
