'''

Задание:

    Создайте класс Person.
    Создайте в классе Person, атрибут name со значением "Vasya".
    Создайте экземпляр id_1 класса Person.
    Создайте в экземпляре id_1, атрибут name со значением "Lena".
    Измените в классе Person атрибут name на значение "Masha".
    Выведите на экран значение атрибута name класса Person, и экземпляра id_1 с помощью print. Каждый результат на отдельной строке, сначала у Person, затем у id_1 (см. пример ниже).

Sample Input:

Sample Output:

Masha
Lena

'''

class Person:
    name = 'Vasya'
id_1 = Person()
id_1.name = 'Lena'
Person.name = 'Masha'
print(Person.name)
print(id_1.name)
