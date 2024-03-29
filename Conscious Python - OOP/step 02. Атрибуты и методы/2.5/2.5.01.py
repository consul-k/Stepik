'''

Вася решил создать приложение Counter (счётчик) для Машеньки, чтобы она училась считать и смогла посчитать количество карточек с покемонами. 
Он решил, что экземпляры ему тут не нужны, и что будет использовать методы класса.
Задание:

    Создайте класс Counter.
    Создайте в классе атрибут count равный нулю.
    Создайте два метода: add_count и set_zero. Оба метода являются методами класса.
    Метод add_count() принимает аргумент по умолчанию add=1, и изменяет атрибут класса count, добавляя к его значению число add. 
    Изначально он добавляет 1, но при желании можно изменить это число. Например, Counter.add_count(5) добавит к значению count число 5, 
    а Counter.add_count() добавит 1.
    Метод  set_zero() изменяет значение атрибута класса count на 0. То есть сбрасывает счётчик.
    Часть кода уже есть. Вам нужно лишь выполнить то, что написано в задании.

Sample Input:

Sample Output:

111

'''

# ваш код:
class Counter:
    count = 0
    @classmethod
    def add_count(cls, add=1):
        cls.count += add
    @classmethod    
    def set_zero(cls):
        cls.count = 0


# код ниже пожалуйста не удаляйте
Counter.add_count()
Counter.set_zero()
Counter.add_count(110)
Counter.add_count()
print(Counter.count)
