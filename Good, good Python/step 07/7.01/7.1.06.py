'''

Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. 
Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', 
а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

Sample Input:

sc_lib@list.ru

Sample Output:

ДА

'''

import re

def check_email_validity(email):
    pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    if re.match(pattern, email):
        return 'ДА'
    else:
        return 'НЕТ'

email = input()
result = check_email_validity(email)
print(result)
