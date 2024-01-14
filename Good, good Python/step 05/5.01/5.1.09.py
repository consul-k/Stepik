'''

Подвиг 10. Гражданин 1 января открыл счет в банке, вложив 1000 руб. Каждый год размер вклада увеличивается на 5% от имеющейся суммы. 
Определить сумму вклада через n лет (n - целое положительное число, вводимое с клавиатуры). Результат округлить до сотых и вывести на экран. 
Программу реализовать при помощи цикла while.

Sample Input:

5

Sample Output:

1276.28

'''

n = int(input())
a = 1000
i = 1
while i <= n:
    a += a * 0.05
    i += 1
print(round(a,2))
