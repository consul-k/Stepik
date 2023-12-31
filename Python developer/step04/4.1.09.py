'''

Давайте напишем своего бота-собеседника. Ваша задача написать программу, которая принимает одну строку на вход. 
И по ней определяет, что нужно ответить человеку.

Бот должен знать команды:

    Привет - Привет!
    Как дела? - Все классно!
    Пока - До скорой встречи!
    Если введена неизвестная команда, нужно вывести сообщение Прости, я еще не знаю таких фраз :(

Рекомендуем использовать знания, полученные в этой главе, например, моржовые операторы и match.

Sample Input 1:

Привет

Sample Output 1:

Привет!

Sample Input 2:

Как дела?

Sample Output 2:

Все классно!

Sample Input 3:

Пока

Sample Output 3:

До скорой встречи!

Sample Input 4:

абракадабра

Sample Output 4:

Прости, я еще не знаю таких фраз :(

'''

match input():
    case "Привет":
        print('Привет!')
    case "Как дела?":
        print('Все классно!')
    case "Пока":
        print('До скорой встречи!')
    case _:
        print('Прости, я еще не знаю таких фраз :(')
