'''

Программа получает на вход список целых чисел и ваша задача вывести каждый третий элемент этого списка, начиная со второго по счету значения.

Гарантируется, что список будет состоять не менее чем из семи элементов.

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

a = list(map(int, input().split()))

Sample Input:

8 32 5 87 2 43 53 23 5

Sample Output:

[32, 2, 23]

'''

a = list(map(int, input().split()))
print(a[1::3])
