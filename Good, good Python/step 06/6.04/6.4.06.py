'''

Подвиг 8. Пользователь с клавиатуры вводит названия городов, пока не введет букву q. 
Определить общее уникальное число городов, которые вводил пользователь. На экран вывести это число. 
Из коллекций при реализации программы использовать только множества.

Sample Input:

Уфа
Москва
Тверь
Екатеринбург
Томск
Уфа
Москва
q

Sample Output:

5

'''

# put your python code here
word = input()
res = set()
while word != 'q':
    res.add(word)
    word = input()
print(len(res))
