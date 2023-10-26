'''

Семья решила заняться оптимизацией своих денежных расходов и придумала следующую схему:

    10 % доходов идут на отпуск
    30 % доходов на пропитание и еду
    5 % на коммунальные платежи
    15 % на выходной досуг
    остальные 40% идут в накопления

Если вдруг нужный процент не получается сделать, тогда копейка перекидывается в накопления. Например:

Сумма доходов равна 50 001.25 , 10 % от этой суммы это 5000.125 рублей. Пол копейки как валюты не существует, поэтому эта половинка переходит в накопления.

Напишите для семьи программу, которая будет принимать на вход месячный доход мужа и жены и расчитывать сколько им нужно отложить на каждую категорию.

Ваша программа принимает два числа типа float. Целая часть – рубли, а дробная – копейки.

В качестве результата работы выведите количество рублей и копеек для каждой из категорий в таком формате:

Отпуск: 10 руб. 5 коп.
Пропитание и еда: 30 руб. 15 коп.
Коммунальные платежи: 5 руб. 0 коп.
Досуг: 10 руб. 11 коп.
Накопления: 50 руб. 3 коп.

Sample Input 1:

30000.50
20000.75

Sample Output 1:

Отпуск: 5000 руб. 12 коп.
Пропитание и еда: 15000 руб. 37 коп.
Коммунальные платежи: 2500 руб. 6 коп.
Досуг: 7500 руб. 18 коп.
Накопления: 20000 руб. 52 коп.

Sample Input 2:

123.45
24.56

Sample Output 2:

Отпуск: 14 руб. 80 коп.
Пропитание и еда: 44 руб. 40 коп.
Коммунальные платежи: 7 руб. 40 коп.
Досуг: 22 руб. 20 коп.
Накопления: 59 руб. 21 коп.

Sample Input 3:

123
234

Sample Output 3:

Отпуск: 35 руб. 70 коп.
Пропитание и еда: 107 руб. 10 коп.
Коммунальные платежи: 17 руб. 85 коп.
Досуг: 53 руб. 55 коп.
Накопления: 142 руб. 80 коп.

Sample Input 4:

100
200

Sample Output 4:

Отпуск: 30 руб. 0 коп.
Пропитание и еда: 90 руб. 0 коп.
Коммунальные платежи: 15 руб. 0 коп.
Досуг: 45 руб. 0 коп.
Накопления: 120 руб. 0 коп.

Sample Input 5:

30000.55
20000.75

Sample Output 5:

Отпуск: 5000 руб. 13 коп.
Пропитание и еда: 15000 руб. 39 коп.
Коммунальные платежи: 2500 руб. 6 коп.
Досуг: 7500 руб. 19 коп.
Накопления: 20000 руб. 53 коп.

Sample Input 6:

32344.45
34543.23

Sample Output 6:

Отпуск: 6688 руб. 76 коп.
Пропитание и еда: 20066 руб. 30 коп.
Коммунальные платежи: 3344 руб. 38 коп.
Досуг: 10033 руб. 15 коп.
Накопления: 26755 руб. 9 коп.

Sample Input 7:

30000.55
20000.85

Sample Output 7:

Отпуск: 5000 руб. 14 коп.
Пропитание и еда: 15000 руб. 42 коп.
Коммунальные платежи: 2500 руб. 7 коп.
Досуг: 7500 руб. 21 коп.
Накопления: 20000 руб. 56 коп.

Sample Input 8:

2000.5
3000.5

Sample Output 8:

Отпуск: 500 руб. 10 коп.
Пропитание и еда: 1500 руб. 30 коп.
Коммунальные платежи: 250 руб. 5 коп.
Досуг: 750 руб. 15 коп.
Накопления: 2000 руб. 40 коп.

Sample Input 9:

2000.55
3000.85

Sample Output 9:

Отпуск: 500 руб. 14 коп.
Пропитание и еда: 1500 руб. 42 коп.
Коммунальные платежи: 250 руб. 7 коп.
Досуг: 750 руб. 21 коп.
Накопления: 2000 руб. 56 коп.

Sample Input 10:

2345.75
3456.55

Sample Output 10:

Отпуск: 580 руб. 23 коп.
Пропитание и еда: 1740 руб. 69 коп.
Коммунальные платежи: 290 руб. 11 коп.
Досуг: 870 руб. 34 коп.
Накопления: 2320 руб. 93 коп.

'''

salary = int(float(input()) * 100 + float(input()) * 100)

vacation = salary * 0.1
food = salary * 0.3
house = salary * 0.05
joy = salary * 0.15
savings = salary * 0.4 + vacation % 1 + food % 1 + house % 1 + joy % 1

print("Отпуск:", int(vacation) // 100, "руб.", int(vacation) % 100, "коп.")
print("Пропитание и еда:", int(food) // 100, "руб.", int(food) % 100, "коп.")
print("Коммунальные платежи:", int(house) // 100, "руб.", int(house) % 100, "коп.")
print("Досуг:", int(joy) // 100, "руб.", int(joy) % 100, "коп.")
print("Накопления:", int(savings) // 100, "руб.", int(savings) % 100, "коп.")
