'''

Если атрибута "name" несуществует, мы его создадим. Все остальные не существующие атрибуты будут возвращать текст.
Задание:

    Создайте класс Person и объявите метод __getattr__.
    В методе __getattr__ создайте условие проверки. Если имя атрибута равно 'name', 
    создайте атрибут name со значением Vasya и верните его значение с помощью return. Иначе верните текст "Такого атрибута нет", с помощью return.
    Создайте экземпляр person
    Выведите на экран значение атрибута name через экземпляр person.  

Sample Input:

Sample Output:

Vasya

'''

class Person:
    def __getattr__(self, item):
        if item == 'name':
            return 'Vasya'
        else:
            return 'Такого атрибута нет'
        
person = Person()
print(person.name)
