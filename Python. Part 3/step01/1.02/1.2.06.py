def find_first_designer(employees):
    for employee in employees:
        if employee["position"] == "Designer":
            return employee
    return None

result = find_first_designer(employees)
print(result)
