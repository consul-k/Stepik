'''

Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.

Напишите программу, которая принимает натуральное число n и находит сумму всех чисел ниже переданного числа n, которые делятся на 3 или на 5.

Sample Input 1:

10

Sample Output 1:

23

Sample Input 2:

9

Sample Output 2:

14

'''

l = []
for i in range(int(input())-1,0,-1):
    if i%3 == 0 or i%5 == 0:
        l.append(i)
print(sum(l))
