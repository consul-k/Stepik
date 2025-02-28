ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}

person = input().strip()

# Используем метод get() для безопасного получения возраста
age = ages.get(person)

# Если возраст не найден, выводим, что возраст неизвестен
if age is None:
    print(f"{person}'s age is unknown.")
else:
    print(f'{person} is {age} years old.')
