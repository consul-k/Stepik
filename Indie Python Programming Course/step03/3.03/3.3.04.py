'''

В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
Входные данные

Размеры зарплат всех сотрудников вводятся в одну строку через пробел. Каждая заработная плата – это натуральное число, не превышающее 105. И гарантируется ,что все зарплаты различны
Выходные данные

Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.

Примечание: функциями min и max, а также сортировками пользоваться нельзя, мы же условный оператор изучаем)

Sample Input 1:

100 500 1000

Sample Output 1:

900

Sample Input 2:

40 30 35

Sample Output 2:

10

Sample Input 3:

567 688 391

Sample Output 3:

297

Sample Input 4:

126 58 152

Sample Output 4:

94

Sample Input 5:

767 93 957

Sample Output 5:

864

Sample Input 6:

661 864 133

Sample Output 6:

731

Sample Input 7:

322 603 954

Sample Output 7:

632

Sample Input 8:

361 252 559

Sample Output 8:

307

Sample Input 9:

551 522 166

Sample Output 9:

385

Sample Input 10:

339 495 401

Sample Output 10:

156

Sample Input 11:

334 738 936

Sample Output 11:

602

'''

a, b, c = map(int, input().split())
if a>b and a>c:
    maxx=a
if b>a and b>c:
    maxx=b 
if c>a and c>b:
    maxx=c        
if a<b and a<c:
    minn=a
if b<a and b<c:
    minn=b
if c<b and c<a:
    minn=c
print(maxx-minn)
