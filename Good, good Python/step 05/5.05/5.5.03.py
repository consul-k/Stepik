'''

Подвиг 4. Вводится четырехзначное целое положительное число. Подумайте, как можно определить итератор для перебора его цифр. 
Выведите цифры этого введенного числа (с помощью итератора) в одну строчку через пробел.

Sample Input:

4387

Sample Output:

4 3 8 7

'''

lst = iter(input())
print(*lst)
