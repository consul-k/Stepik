'''

    Создайте класс Number и объявите в нём два метода: __init__ и __sub__.
    Метод __init__(self, number) создаёт атрибут number со значением number
    Метод __sub__ должен позволять делать вычитание, в формате "экземпляр - экземпляр"
    Создайте два экземпляра num1 и num2, со значением number 70 и 20 соответственно.
    Выведите на экран результат вычитания num1 - num2

Sample Input:


Sample Output:

50

'''

class Number:
    def __init__(self, number):
        self.number = number
    def __sub__(self, other):
        return self.number - other.number

num1 = Number(70)
num2 = Number(20)

result = num1-num2

print(result)
