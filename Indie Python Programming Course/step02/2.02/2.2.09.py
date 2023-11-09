'''

Программа получает на вход одно слово. Ваша задача перенести последнюю букву в начало, тем самым сдвинуть все остальные буквы вправо на один разряд. 
В качестве ответа нужно вывести полученное слово

Sample Input 1:

become

Sample Output 1:

ebecom

Sample Input 2:

come

Sample Output 2:

ecom

Sample Input 3:

qwertY

Sample Output 3:

Yqwert

Sample Input 4:

AbracadabrA

Sample Output 4:

AAbracadabr

'''

a = input()
print(a[-1]+a[:-1])
