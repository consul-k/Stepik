'''

На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения:

ed+ln⁡(d)+lg⁡(d)+sqrt(d)

Формат входных данных
На вход программе подается положительное десятичное число dd.

Формат выходных данных
Программа должна вывести искомое значение выражения.
Подсказка
Используйте методы типа 
Тестовые данные 🟢

Sample Input 1:

1.1

Sample Output 1:

4.189677737079134559844013562

Sample Input 2:

4.0

Sample Output 2:

58.58650438559209208737220323

'''

from decimal import *
from math import *

d = Decimal(input())
result = d.exp() + d.ln() + d.log10() + d.sqrt()
print(result)
