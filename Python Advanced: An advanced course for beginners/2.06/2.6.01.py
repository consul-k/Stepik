# Список предметов
lst = ['нож', 'пистолет', 'фонарь', 'крест', 'рукоять от меча']

# Далее Ваш код
a, b, c = input(), input(), input()
if a not in lst:
    lst.append(a)
if b not in lst:
    lst.append(b)
if c not in lst:
    lst.append(c)

print('Снаряжение обновлено:',lst)
