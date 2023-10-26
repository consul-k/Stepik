'''

Вашей программе на вход даются 3 строки. Выведите обратно строку наименьшей длины. 
В случае, если длина у нескольких строк совпадает – выведите ту, которая была введена позже остальных.

Напоминаем, что посчитать длину строки можно с помощью len.

s = "abc"
print(len(s))  # 3

print(len("abcaba"))  # 6

Sample Input 1:

first
second
third

Sample Output 1:

third

Sample Input 2:

first
third
second

Sample Output 2:

third

Sample Input 3:

py
pyth
python

Sample Output 3:

py

Sample Input 4:

py
th
on

Sample Output 4:

on

Sample Input 5:

pyth
py
python

Sample Output 5:

py

Sample Input 6:

pyth
python
py

Sample Output 6:

py

Sample Input 7:

python
pyth
py

Sample Output 7:

py

'''

n1 = input()
n2 = input()
n3 = input()

if len(n1) >= len(n2):
    n1 = n2
if len(n1) >= len(n3):
    n1 = n3
print(n1)
