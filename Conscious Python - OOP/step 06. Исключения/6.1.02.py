'''

Машенька доработала свой трансформатор красоты, теперь он работает как надо. Но при желании, программа может превратить человека в индюка, 
если специально указать вместо веса, слово "Индюк". Так как Машенька ещё держит обиду на Васю, она решает на время превратить его в индюка, 
заманив его в свой аппарат.
Задание:

    Создайте класс BeuatyTransform и два метода: __init__, transformer.
    Метод __init__ принимает два аргумента: height, weight и создаёт два атрибута height, weight с этими же значениями. 
    Также, __init__ создаёт атрибут result = "Божественная красота".
    Метод transformer(self) содержит внутри конструкцию try-except-else-finally:
    - В блоке try cоздаётся атрибут new_body равный делению self.height / self.weight
    - Блок except проверяет код на разные ошибки, поэтому применяется except Exception. Если ошибка обнаружится, атрибут result получает новое значение: 
    "Индюк на три дня"
    - Блок else выводит сообщение на экран: Проверка прошла! В print() также используется end=' '
    - Блок finally выводит сообщение на экран: Результат: result. Где result - это значение атрибута result.
    Часть кода уже написана, вам нужно лишь сделать задание выше.

Sample Input:

Sample Output:

Проверка прошла! Результат: Божественная красота
Проверка прошла! Результат: Божественная красота
Результат: Индюк на три дня

'''

# Создайте класс и методы
class BeuatyTransform:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.result = 'Божественная красота'
    def transformer(self):
        try:
            self.new_body = self.height / self.weight
        except Exception:
            self.result = 'Индюк на три дня'
        else:
            print('Проверка прошла!', end=' ')
        finally:
            print(f'Результат: {self.result}')

# Код ниже пожалуйста не меняйте, ради Васи
nastya = BeuatyTransform(100, 50)
lena = BeuatyTransform(50, 90)
vasya = BeuatyTransform(172, "Индюк")

nastya.transformer()
lena.transformer()
vasya.transformer()
