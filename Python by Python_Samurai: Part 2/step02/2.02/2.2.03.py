employees = [
    {
        'name': 'Alex',
        'position': 'director',
        'salary': 1000000
    },
{
        'name': 'Marty',
        'position': 'security',
        'salary': 50000
    },
{
        'name': 'Gloria',
        'position': 'accountant',
        'salary': 150000
    }
]

# продолжите решение здесь
a = employees.copy()
for d in a:
    del d['salary']
print(a)
