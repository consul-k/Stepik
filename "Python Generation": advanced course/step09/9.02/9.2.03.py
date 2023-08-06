'''

Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, 
однако к концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

Формат входных данных
На вход программе в первой строке подаётся натуральное число n – количество названных городов, 
в последующих n строках вводятся названные города и ещё одна строка с новым, только что названым городом.

Формат выходных данных
Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.
Тестовые данные 🟢

Sample Input 1:

3
Каир
Рим
Москва
Агра

Sample Output 1:

OK

Sample Input 2:

5
Лас-Вегас
Сеул
Лондон
Ницца
Адел
Лас-Вегас

Sample Output 2:

REPEAT

Sample Input 3:

2
Паттайя
Якутск
Казань

Sample Output 3:

OK

'''

n = int(input())
cities = set()
repeat = False

for _ in range(n+1):
    city = input()
    if city in cities:
        repeat = True
    cities.add(city)
    
if repeat:
    print('REPEAT')
else:
    print('OK')
