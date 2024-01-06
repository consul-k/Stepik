'''

    Часть кода уже написана. Переменная names содержит список имён.
    Проверить, есть ли в списке names, имена атрибутов класса Person.
    Если имя в списке и имя атрибута в классе совпадают, удалите атрибут из класса.
    Ваша задача, только проверить и удалить совпадающие атрибуты, всё остальное уже готово.

 

# напоминашка
delattr(object, name)
# object - объект, у которого нужно удалить атрибут.
# name - имя атрибута, который нужно удалить.

Sample Input:

Sample Output:

6

'''

names = ['Klementina', 'Roza', 'Balu', 'Lena', 'Leonid']  # список имён

class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''

# ниже ваш код:
for name in names:
    if hasattr(Person, name):
        delattr(Person, name)

# строки ниже не удаляйте, ради вселенной:
print(len(Person.__dict__))
