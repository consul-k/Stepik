'''

Создайте функцию count_letters, которая принимает на вход фразу и подсчитывает, какое количество в ней строчных(K) и заглавных (N) букв, 
все остальные символы игнорируются. Функция должна вывести на экран информацию о найденных буквах в определенном формате. 

Количество заглавных символов: N
Количество строчных символов: K

Вам необходимо написать только определение функции count_letters.

Sample Input 1:

Привет, Старина

Sample Output 1:

Количество заглавных символов: 2
Количество строчных символов: 11

Sample Input 2:

QWERTY

Sample Output 2:

Количество заглавных символов: 6
Количество строчных символов: 0

'''

def count_letters(word):
    cnt_upper = 0
    cnt_lower = 0
    for i in word:
        if i.isupper():
            cnt_upper += 1
        elif i.islower():
            cnt_lower += 1
    print(f'Количество заглавных символов: {cnt_upper}')
    print(f'Количество строчных символов: {cnt_lower}')
