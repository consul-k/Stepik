employees = {
    "emp1": {"name": "John", "age": 29, "department": "HR"},
    "emp2": {"name": "Anna", "age": 24, "department": "IT"},
    "emp3": {"name": "Mike", "age": 31, "department": "IT"},
    "emp4": {"name": "Sara", "age": 27, "department": "HR"}
}

result = [
    emp["name"]
    for emp in employees.values()
    if emp["department"] == "IT" and emp["age"] > 25
]

print(result)
