'''

    Создайте класс Number и объявите метод __init__. Метод имеет аргументы (self, number), и создаёт атрибут number со значением number.
    Объявите метод __add__ (self, other) который позволяет складывать экземпляры с экземплярами, а также экземпляры с числами. Учтите, что при сложении, будет складываться атрибут "number + number" двух экземпляров, и "number + число".
    Создайте два экземпляра num1 и num2, с атрибутом number равным 100 и 200 соответственно.
    Выведите на экран результаты трёх сложений, каждый на отдельной строке:
    num1 + num2
    num1 + 300
    num2 + 300
    Результат сложения будет число, смотрите пример ответа ниже.

Sample Input:

Sample Output:

300
400
500

'''

class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Number):
            return self.number + other.number
        if isinstance(other, int):
            return self.number + other
        
num1 = Number(100)
num2 = Number(200)

print(num1 + num2)
print(num1 + 300)
print(num2 + 300)
