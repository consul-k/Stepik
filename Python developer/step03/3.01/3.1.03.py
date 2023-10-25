'''

На вход вашему серверу пришло время в минутах, которое провел пользователь на сайте , а также время начала сессии.
Вам нужно определить сколько времени было на цифровых часах у пользователя, когда он закрывал сайт.

Ваша программа получает на вход 3 переменные, каждая в новой строке:

    time_mins – количество минут, которое пользователь провел на сайте
    start_hours – время в часах, когда пользователь зашел на сайт
    start_mins – время в минутах, когда пользователь зашел на сайт

Программа должна вывести через пробел количество часов и минут, когда пользователь закрыл сайт

Sample Input 1:

120
19
0

Sample Output 1:

21 0

Sample Input 2:

125
23
5

Sample Output 2:

1 10

Sample Input 3:

0
0
0

Sample Output 3:

0 0

Sample Input 4:

0
20
20

Sample Output 4:

20 20

Sample Input 5:

125
0
0

Sample Output 5:

2 5

Sample Input 6:

119
19
30

Sample Output 6:

21 29

'''

time_mins, start_hours, start_mins = int(input()), int(input()), int(input())
s = time_mins + start_mins + start_hours * 60
print((s//60)%24, (start_mins+time_mins)%60)
