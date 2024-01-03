'''

    Создайте класс Number и объявите два метода: __init__ и __truediv__
    Метод __init__(self, number) создаёт атрибут number со значением number
    Метод __truediv__(self, other) возвращает результат деления number на other. Создайте проверку:
    - Если other является 0, верните строку "на ноль делить нельзя".
    - Если не 0, то просто верните результат деления number на other.
    Создайте экземпляр num, с атрибутом number равным числу 10
    Выведите на экран результат деления экземпляра num на число 2 и на 0. Два результата запишите на отдельных строках.

Sample Input:

Sample Output:

5.0
на ноль делить нельзя

'''

class Number:
    def __init__(self, number):
        self.number = number
    def __truediv__(self, other):
        if other == 0:
            return "на ноль делить нельзя"
        else:
            return self.number / other

num = Number(10)
print(num / 2)
print(num / 0)
