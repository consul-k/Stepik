'''

    Создайте любой класс.
    Создайте метод класса с любым названием, используя декоратор @classmethod. В скобках метода укажите три аргумента: (cls, x, y)
    В теле метода класса будет выполняться создание атрибутов "x" и "y" со значениями аргументов "x" и "y" соответственно. Например cls.x = x. 
    Там же в теле метода, будет выполняться умножение "x" на "y", и выводиться на экран результат с помощью print.
    Вызовите созданный вами метод через класс, и укажите в аргументах число 5 и 20. При вызове не нужно использовать print. Пример вызова: Класс.метод(5, 20).

Sample Input:

Sample Output:

100

'''

class Math:
    @classmethod
    def mult(cls, x, y):
        cls.x = x
        cls.y = y
        print(cls.x*cls.y)

Math.mult(5,20)
