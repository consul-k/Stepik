'''

Вася использует программирование в повседневной жизни. В этот раз он пишет программу, показывающую истёк ли срок годности у товара или нет. 
Он указывает сегодняшнюю дату и дату окончания товара и получает ответ. Для этого он нестерпимо решил использовать статический метод.
Задание:

    Часть кода уже написана. Для выполнения задания, уже импортирована библиотека datetime. 
    С помощью этой библиотеки мы создадим сегодняшнюю дату (start) и дату окончания (finish). 
    И после этого, мы сможем сравнивать эти даты на "больше, меньше, равно", как обычные числа.
    Создайте класс Product.
    Создайте статический метод check_date(today, expiry). Аргумент today - это сегодняшняя дата, а аргумент expiry - дата срока годности товара. 
    В методе создадим две переменные start и finish:
    start = datetime.strptime(today, "%Y-%m-%d")
    finish = datetime.strptime(expiry, "%Y-%m-%d")
    Сравните finish и start. Если finish больше чем start выведите текст: Срок годности в порядке.
    Иначе выведите текст: Срок годности истёк.
    Вам нужно только сделать то, что в задании, остальное уже готово.

Sample Input:

Sample Output:

Срок годности в порядке
Срок годности истёк
Срок годности истёк

'''

from datetime import datetime

# ваш код:
class Product:
    @staticmethod
    def check_date(today, expiry):
        start = datetime.strptime(today, "%Y-%m-%d")
        finish = datetime.strptime(expiry, "%Y-%m-%d")
        if finish > start:
            print('Срок годности в порядке')
        else:
            print('Срок годности истёк')



# код ниже пожалуйста не удаляйте
today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)
