'''

Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, 
на которых встречается число xx в переданном списке lstlst.

Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:

5 8 2 7 8 8 2 4
8

Sample Output 1:

1 4 5

Sample Input 2:

5 8 2 7 8 8 2 4
10

Sample Output 2:

Отсутствует

'''

lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
    
elif x in lst:
    count = lst.count(x)
    z = lst.index(x)
    print(z,end=' ')
    while count != 0:
        if x in lst[z+1:]:
            count-=1
            z = lst.index(x,z+1,)
            print(z,end=' ')
        elif x not in lst[z+1:]:
            break
