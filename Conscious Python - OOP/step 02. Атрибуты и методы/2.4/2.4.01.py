'''

Задание:

    Создайте класс Kitty.
    Создайте метод print_cat (не забудьте про self).
    Внутри метода создайте print('Hello, Kitty'). Метод выводит на экран строку 'Hello, Kitty'.
    Создайте экземпляр cat.
    Вызовите метод через экземпляр cat.метод(), чтобы вывести на экран текст. Функцию print использовать не нужно.

Sample Input:

Sample Output:

Hello, Kitty

'''

class Kitty:
    def print_cat(self):
        print('Hello, Kitty')
        
cat = Kitty()
cat.print_cat()
