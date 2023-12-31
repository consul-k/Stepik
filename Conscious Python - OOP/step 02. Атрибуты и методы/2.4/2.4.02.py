'''

Задание:

Часть кода уже есть, вам нужно:

    Создать метод, назовите его как пожелаете. Помните, что имя метода означает - глагол, действие, поэтому подберите соответствующее название.
    Метод выводит на экран надпись: "Привет, атрибут". Но слово "атрибут" замените, на значение атрибута name. У каждого экземпляра свой атрибут name, поэтому и значения будут разными. Подсказка, можно использовать f-строку.
    Вызовите метод у каждого экземпляра. Не забывайте скобки, при вызове метода. Функцию print использовать не нужно.
    Примеры ответов есть ниже.

Sample Input:

Sample Output:

Привет, Bart
Привет, Lisa
Привет, Gomer

'''

class Simpsons:
    name = 'Simpsons'
    # здесь будет ваш метод
    def say_hi(self):
        print(f'Привет, {self.name}')

bart = Simpsons()
bart.name = 'Bart'

lisa = Simpsons()
lisa.name = 'Lisa'

gomer = Simpsons()
gomer.name = 'Gomer'

# здесь будет ваш код вызова метода:
bart.say_hi()
lisa.say_hi()
gomer.say_hi()
