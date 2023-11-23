'''

Напишите функцию replace, которая принимает три параметра:

    обязательный строковый параметр text - текст, в котором необходимо выполнить замены;
    обязательный строковый параметр old - строка поиска для замены;
    необязательный строковый параметр new - значение замены для найденного значения old. По умолчанию равен пустой строке.

Функция replace должна возвращать новую строку, в которой все символы old были заменены на new. При замене регистр букв должен учитываться

replace('Нет', 'т') => 'Не'
replace('Bella Ciao', 'a') => 'Bell Cio'
replace('nobody; i myself farewell analysis', 'l', 'z') => 'nobody; i mysezf farewezz anazysis'
replace('commend me to my kind lord meaning', 'M', 'w') => 'commend me to my kind lord meaning'

Ваша задача дописать только тело функции replace

'''

def replace(text: str, old: str, new: str = ''):
    s = ''
    for i in text:
        if i == old:
            s += new
        else:
            s += i
    return s
