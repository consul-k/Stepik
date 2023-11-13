'''

Давайте составим сводную информацию о квадратах и кубах интервала чисел.

На вход программе подается два натуральных числа a и b (гарантируется, что a<b), 
после чего для каждого целого числа на интервале от a до b включительно необходимо вывести фразу следующего вида:

«Число {число}; его квадрат = {квадрат}; его куб = {куб}»

Кавычки выводить не нужно и пользуйтесь f-строкой.

Формат входных данных
На вход программе подается два натуральных числа a и b, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

1
5

Sample Output 1:

Число 1; его квадрат = 1; его куб = 1
Число 2; его квадрат = 4; его куб = 8
Число 3; его квадрат = 9; его куб = 27
Число 4; его квадрат = 16; его куб = 64
Число 5; его квадрат = 25; его куб = 125

Sample Input 2:

35
43

Sample Output 2:

Число 35; его квадрат = 1225; его куб = 42875
Число 36; его квадрат = 1296; его куб = 46656
Число 37; его квадрат = 1369; его куб = 50653
Число 38; его квадрат = 1444; его куб = 54872
Число 39; его квадрат = 1521; его куб = 59319
Число 40; его квадрат = 1600; его куб = 64000
Число 41; его квадрат = 1681; его куб = 68921
Число 42; его квадрат = 1764; его куб = 74088
Число 43; его квадрат = 1849; его куб = 79507

'''

a, b = int(input()), int(input())
for i in range(a, b+1):
    print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')
