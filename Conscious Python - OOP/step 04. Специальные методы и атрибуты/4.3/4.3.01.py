'''

    Создайте класс Number и объявите в нём два метода: __init__ и __eq__
    Метод __init__ :
    - В аргументах принимает (self, x, y).
    - Создаёт атрибут "summa", равный сумме аргументов "x" и "y".
    Метод __eq__(self, other) содержит два условия:
    - Если объект other является объектом класса Number, то возвращается (return) результат сравнения (==) атрибутов "summa" у двух экземпляров класса.
    - Если объект other является числом (int), то возвращается (return) результат сравнения (==) атрибута "summa" у экземпляра класса с числом.
    Создаются два экземпляра number_1 и number_2. При создании, number_1 принимает "x" и "y" равный 4 и 2, так как объявлен __init__. 
    При создании, number_2 принимает "x" и "y" равный 5 и 5.
    Выведите на экран результат трёх сравнений, каждый на отдельной строке.
    - сравните number_1 и number_2 (==)
    - сравните number_1 с числом 10 (==)
    - сравните number_2 с числом 10 (==)

Напоминашка:
__eq__ # равно
__ne__ # не равно

Sample Input:

Sample Output:

False
False
True

'''

class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.summa = self.x + self.y
        
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.summa == other.summa
        if isinstance(other, int):
            return self.summa == other
        
    def __ne__(self, other):
        return not self.__eq__(other)

number_1 = Number(4,2)
number_2 = Number(5,5)

print(number_1 == number_2)
print(number_1 == 10)
print(number_2 == 10)
