'''

Программиста Тихона попросили написать программу, которая должна была сравнивать две введенные строки на равенство, при этом не учитывая регистр букв. Если строки вводились одинаковые, программа Тихона должна была печатать True, в противном случае False

Но что-то пошло не так. Тихон написал программу, в которой есть ошибки. Ваша задача исправить имеющуюся программу так, чтобы она прошла все тесты. 

Sample Input 1:

Hello
hEllO

Sample Output 1:

True

Sample Input 2:

Что в коробке?
ЧТО В коРобКе?

Sample Output 2:

True

Sample Input 3:

qwert
qwe

Sample Output 3:

False

Sample Input 4:

u2
u3

Sample Output 4:

False

'''

s = input()
word = input()
print(s.upper() == word.upper())
