'''

Представьте, что у вас есть формочка на сайте для ввода строк. Ваш менеджер сказал вам, что в этой формочке обязательно должны быть строки из первого множества, а так же опционально можно добавить строки из второго, или не добавлять вообще. Проверьте, что множество строк, которое ввел вам пользователь в эту формочку подходит по заданным условиям.

Вашей программе на вход поступают 3 множества. Каждое на отдельной строке. Элемент множеств отделены друг от друга пробелом.

    Первое множество – обязательные строки
    Второе множество – опциональные строки
    Третье множество – строки введенные пользователем

Выведите True, если пользователь ввел все правильно и False, если ошибся.

Ввод:

required – множество обязательных строк

optional – множество опциональных строк

user_data – множество строк, которые ввел пользователь строк

Вывод:

True или False в зависимости от результата работы программы

Sample Input 1:

login password
name surname
login password name

Sample Output 1:

True

Sample Input 2:

login password
name surname
login password name surname virus

Sample Output 2:

False

Sample Input 3:

1 2
3 4
1 2 3 4

Sample Output 3:

True

Sample Input 4:

1 2
3 4
1 2

Sample Output 4:

True

Sample Input 5:

1 2
3 4
1

Sample Output 5:

False

Sample Input 6:

1 2
3 4
3 4

Sample Output 6:

False

Sample Input 7:

1 2
3 4 5
1 2 3 4 5 6

Sample Output 7:

False

'''

a=set(input())
b=set(input())
c=set(input())
if b&c|a==c:
    print(True)
else:
    print(False)
