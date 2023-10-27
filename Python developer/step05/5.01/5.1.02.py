'''

Иногда нужно сложить две строки между собой, для этого достаточно написать +.

s1 = "ab"
s2 = "cd"

s3 = s1 + s2
print(s3)  # abcd

Задача на программирование

Напишите программу, которая перебирает значения переменной values и печатает их с восклицательными знаками.

Sample Input 1:

привет мир

Sample Output 1:

привет!
мир!

Sample Input 2:

мой сигнал этому миру уже послан

Sample Output 2:

мой!
сигнал!
этому!
миру!
уже!
послан!

Sample Input 3:

1 2 3 4

Sample Output 3:

1!
2!
3!
4!

Sample Input 4:

a

Sample Output 4:

a!

Sample Input 5:

a b

Sample Output 5:

a!
b!

'''

values = input().split()
for i in values:
    print(i+'!')
