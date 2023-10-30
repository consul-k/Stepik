'''

Напишите программу-дешифратор шифра цезаря

Ввод:

s – строка состоящая из букв a-z

step – шаг шифра, натуральное число

Вывод:

res – расшифрованная строка

Sample Input:

def
3

Sample Output:

abc

'''

s = input()
step = int(input())
new_letter = 0
res = ''
for letter in s:
    new_letter = (ord(letter) - step - 97) % 26 + 97
    res += chr(new_letter)
print(res)
