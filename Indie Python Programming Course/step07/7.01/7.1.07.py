'''

Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :

    Есть хотя бы 3 цифры
    Есть хотя бы одна заглавная буква 
    Есть хотя бы один символ из следующего набора "!@#$%*"
    Общая длина не менее 10 символов

Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

Вам необходимо написать только определение функции check_password

Разбор Youtube Patreon Boosty

Sample Input 1:

qwerty

Sample Output 1:

Easy peasy

Sample Input 2:

Qwerty1357!

Sample Output 2:

Perfect password

Sample Input 3:

Qwerty1357)

Sample Output 3:

Easy peasy

Sample Input 4:

Qwerty17!

Sample Output 4:

Easy peasy

'''

def check_password(password):
    check_1 = False
    check_2 = False
    
    ch_3_set = {'!', '*', '%', '@', '$', '#'}
    check_3 = False

    check_4 = False
    
    if len(password) >= 10:
        check_4 = True
        
    cnt = 0
    cnt_dig = 0
    for i in password:
        if i in ch_3_set:
            cnt += 1
        if cnt >= 1:
            check_3 = True
        if i.istitle():
            check_2 = True
        if i.isdigit():
            cnt_dig+=1
        if cnt_dig >= 3:
            check_1 = True
    if check_1 == check_2 == check_3 == check_4 == True:
        print('Perfect password')
    else:
        print('Easy peasy')
