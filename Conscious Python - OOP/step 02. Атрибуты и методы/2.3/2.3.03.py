'''

    Часть кода уже написана.
    Создайте экземпляр id_1 класса Person. Не забывайте про скобки Person().
    С помощью getattr(), выведите на экран значения трёх атрибутов, используя экземпляр. Каждое значение выводится на отдельной строке, начиная с dance, смотрите пример вывода ниже.

 

​# напоминашка
getattr(object, name, default)
# object - класс или экземпляр, у которого вы хотите получить атрибут.
# name - атрибут, значение которого вы хотите получить. 
# default (необязательный аргумент) - значение, которое будет возвращено, если атрибут не существует. 

Sample Input:

Sample Output:

dance
design
college

'''

class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'

attr = ['hobby', 'work', 'study']
id_1 = Person()
for a in attr:
    print(getattr(id_1, a, False))
