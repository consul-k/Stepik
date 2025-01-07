def cut_name(lst):
    for n in lst:
        yield n[:4]

my_list = ['Алон', 'Эйли', 'Крут Кобэйн', 'Стивен Сингл']

names = cut_name(my_list)
print(next(names))  # Алон
print(next(names))  # Эйли
print(next(names))  # Крут
print(next(names))  # Стив
