lst = [{'Вадим Петров': 'm'}, {'Анна Хетуей': 'f'},
       {'Гарри Поттер': 'm'}, {'Дарья Сыроежкина': 'f'},
       {'Олег Семёнов': 'm'}, {'Хлоя Моретц': 'f'},
       {'Арнольд Газманов': 'm'}, {'Фрида Капуэйра': 'f'}]

# продолжите решение здесь
def func(lst):
    males = [person for person in lst if list(person.values())[0] == 'm']
    females = [person for person in lst if list(person.values())[0] == 'f']

    result = []
    for male in males:
        lastname = list(male.keys())[0].split()[1]
        for female in females:
            firstname = list(female.keys())[0].split()[0]
            if lastname.endswith('ов') or lastname.endswith('ев') or lastname.endswith('ин'):
                result.append(f"{firstname} {lastname}а")
            else:
                result.append(f"{firstname} {lastname}")

    return result

new_lst = func(lst)
print(*new_lst, sep="\n")
