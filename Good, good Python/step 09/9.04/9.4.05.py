'''

Подвиг 5. Вводится список email-адресов в одну строчку через пробел. 
Среди них нужно оставить только корректно записанные адреса. Будем полагать, что к таким относятся те, что используют латинские буквы, 
цифры и символ подчеркивания. А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел.

Sample Input:

abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com

Sample Output:

abc@it.ru biba123@list.ru sc_lib@list.ru

'''

# put your python code here
import re

def check_email_validity(email):
    pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    if re.match(pattern, email):
        return email

mails = input().split()
check = filter(check_email_validity, mails)
print(*check)
