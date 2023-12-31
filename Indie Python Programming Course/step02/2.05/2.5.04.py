'''

Программе поступают последовательно три числа: значения оттенка красного, потом зеленого и затем синего цветов. 
Данные числа варьируются от 0 до 255 включительно
Выходные данные

Ваша задача закодировать оттенки цветов согласно RGB модели.

Не забывайте, что на каждый цвет всегда должно отводиться два разряда. Символы букв в шестнадцатеричной системе необходимо записывать в верхнем регистре.

Примечание: для перевода в 16-ую систему вы можете воспользоваться функцией hex, она возвращает строку перевода в 16ую систему,
впереди которой находятся два служебных знака 0x

Sample Input 1:

1
2
3

Sample Output 1:

#010203

Sample Input 2:

0
255
10

Sample Output 2:

#00FF0A

Sample Input 3:

75
0
130

Sample Output 3:

#4B0082

Sample Input 4:

143
0
255

Sample Output 4:

#8F00FF

Sample Input 5:

154
73
55

Sample Output 5:

#9A4937

'''

r = hex(int(input()))[2:].zfill(2).upper()
g = hex(int(input()))[2:].zfill(2).upper()
b = hex(int(input()))[2:].zfill(2).upper()
print('#'+r+g+b)
