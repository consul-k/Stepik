'''

Подвиг 4. Вводится порядковый номер дня недели (1, 2, ..., 7). 
Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье). 
Программу реализовать с использованием операторов if-elif.

Sample Input:

2

Sample Output:

вторник

'''

day = {1: 'понедельник',
       2: 'вторник',
       3: 'среда',
       4: 'четверг',
       5: 'пятница',
       6: 'суббота',
       7: 'воскресенье'
      }
print(day[int(input())])
