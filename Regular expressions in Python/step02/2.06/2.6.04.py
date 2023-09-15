'''

Напишите регулярное выражение, которое найдёт все цифры из шестнадцатеричной системы счисления.

Что нужно найти:

Цифры из шестнадцатеричной системы счисления: 0123456789ABCDEF

Sample Input 1:

<=>@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;

Sample Output 1:

A B C D E F 0 1 2 3 4 5 6 7 8 9

Sample Input 2:

#03B6FC

Sample Output 2:

0 3 B 6 F C

Sample Input 3:

٠١٢٣٤٥٦٧٨٩

Sample Output 3:

'''

regex = r'[0-9A-F]'
