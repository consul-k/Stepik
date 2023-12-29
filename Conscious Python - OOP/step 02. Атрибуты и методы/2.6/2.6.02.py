'''

    Часть кода уже написана.
    Выведите на экран, значения всех атрибутов экземпляра person1. Каждое значение должно быть на отдельной строчке. 
    Можете сделать простым способом, а можете попробовать через цикл, в любом случае используйте __dict__. 

Sample Input:

Sample Output:

Vasya
20
driver

'''

class Person:
    pass

person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}

# ваш код ниже:
for i in person_1.__dict__.values():
    print(i)
