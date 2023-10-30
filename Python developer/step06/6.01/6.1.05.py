'''

На вход программе подается строка состоящая из букв латинского алфавита в нижнем регистре, которую нужно зашифровать и сдвиг, на который нужно сдвинуть буквы в слове. Проверка на сдвиг вне диапазона 1-26 не проводится.

Ввод:

s – строка состоящая из букв a-z

step – шаг шифра, натуральное число

Вывод:

res – зашифрованная шифром строка

Sample Input 1:

abc
3

Sample Output 1:

def

Sample Input 2:

zzzbbb
1

Sample Output 2:

aaaccc

Sample Input 3:

abcdefghijklmnopqrstuvwxyz
5

Sample Output 3:

fghijklmnopqrstuvwxyzabcde

'''

s = input()
step = int(input())
new_letter = 0
res = ''
for letter in s:
    new_letter = (ord(letter) + step - 97) % 26 + 97
    res += chr(new_letter)
print(res)
