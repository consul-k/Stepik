'''

Напишите программу, которая получает на вход строку, и выводит каждый ее символ умноженный на индекс + 1.

Используйте для решения задачи цикл for со счетчиком или for в комбинации с enumerate.

Ввод:

s – строка

Вывод:

Строки, содержащие символы строки s умноженные на индекс+1

Sample Input 1:

back

Sample Output 1:

b
aa
ccc
kkkk

Sample Input 2:

a

Sample Output 2:

a

Sample Input 3:

abcdef

Sample Output 3:

a
bb
ccc
dddd
eeeee
ffffff

'''

s = input()
for idx, letter in enumerate(s):
    print(letter*(idx+1))
