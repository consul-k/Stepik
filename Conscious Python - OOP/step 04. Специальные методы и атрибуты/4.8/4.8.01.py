'''

Маша, Вика и Лена, ещё только учатся считать, поэтому могут ошибиться. 
Они взяли одинаковый товар на 1000 и подошли на кассу расплатиться. Каждый из них достал денежку (number) и посчитал как мог, проверьте, 
достаточно ли они положили денег на кассе. И не переживайте, денежки у них есть, просто могут ошибиться в подсчёте. 
Задание:

    Часть кода уже написана.
    Добавьте недостающий код, только в методе __new__.
    В методе __new__ сделайте проверку, если number меньше 1000, то экземпляр не создаётся. Если больше, то экземпляр создастся. 
    Чтобы отменить создание экземпляра, можете использовать pass.

Sample Input:


Sample Output:

False
True
True

'''

class StopNumber:
    def __new__(cls, number, name):
        if number < 1000:
            pass
        else:
            return super().__new__(cls)

    def __init__(self, number, name):
        self.number = number
        self.name = name

# Код ниже пожалуйста не меняйте
Masha = StopNumber(500, 'Masha')
Vika = StopNumber(1500, 'Vika')
Lena = StopNumber(1200, 'Lena')

print(isinstance(Masha, StopNumber))
print(isinstance(Vika, StopNumber))
print(isinstance(Lena, StopNumber))
