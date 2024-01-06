'''

Машенька обиделась на Васю, и сказала, что с ним не будет разговаривать какое-то время. 
Но Васе нужно узнать у Машеньки, куда она положила активатор телепорта. Поэтому Вася сообразил, и решил узнать информацию через Маму, 
чтобы Мама спросила у Машеньки, а потом рассказала Васе.

Задание:

    Импортируйте модуль accessify (from accessify import private)
    Создайте класс Teleport
    Создайте приватный метод __activator_teleport(), используя декоратор @private. Метод выводит на экран информацию:
    "Активатор от телепорта у Машеньки под подушкой".
    Создайте публичный метод mama_help(). Метод возвращает приватный метод  __activator_teleport().
    К сожалению, на Stepik нет модуля accessify. Поэтому задание выполните у себя на компьютере, например в PyCharm. Часть кода уже написана, сюда вставьте ваш код из PyCharm, но без импорта модуля и без декоратора. Либо закомментируйте импорт и декоратор. Не забывайте про self и скобки при вызове методов.

Sample Input:

Sample Output:

Активатор от телепорта у Машеньки под подушкой

'''

# импортируйте модуль, объявите класс, и нужные методы
#from accessify import private

class Teleport:
    #@private
    def __activator_teleport(self):
        print('Активатор от телепорта у Машеньки под подушкой')
        
    def mama_help(self):
        self.__activator_teleport()

# код ниже пожалуйста не удаляйте
vasya = Teleport()
vasya.mama_help()
