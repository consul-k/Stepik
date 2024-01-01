'''

    Создайте класс Number и объявите в нём два метода (__init__, __delattr__).
    Метод __init__ :
    - содержит аргументы (self, a, b)
    - создаёт атрибуты "a", "b" с соответствующими значениями a, b
    - создаёт атрибут "s" который равен сумме "a + b"
    - удаляет атрибут "s"
    Метод __delattr__ :
    - содержит аргументы (self, name)
    - содержит условие, если атрибут "s" больше 10, то ничего не делаем (pass). Иначе производим стандартное удаление с помощью super().__delattr__(name)
    Код проверки не удаляйте, пожалуйста

Sample Input:


Sample Output:

False
True

'''

# ваш код:
class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = self.a + self.b
        del self.s
    def __delattr__(self, name):
        if self.s > 10:
            pass
        else:
            super().__delattr__(name)


# код проверки:
number1 = Number(4, 5)
print('s' in number1.__dict__)

number2 = Number(6, 11)
print('s' in number2.__dict__)
