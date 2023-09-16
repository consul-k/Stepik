'''

Напишите регулярное выражение, которое найдёт четырёхбуквенное слово в начале строки.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из 4 букв
    Используется латинский и кириллический алфавиты верхнего и нижнего регистров
    Стоит в начале строки
    Справа от последовательности граница слова (вспомните, с помощью чего мы её определяли в прошлом задании)

Sample Input 1:

Курс доллара упал до 27394239 рублей

Sample Output 1:

Курс

Sample Input 2:

Если волк молчит, то лучше его не перебивать

Sample Output 2:

Если

Sample Input 3:

Это трёхбуквенное слово

Sample Output 3:

Sample Input 4:

Also I would like to...

Sample Output 4:

Also

Sample Input 5:

 перед первым словом стоит пробел

Sample Output 5:

Sample Input 6:

.test

Sample Output 6:

Sample Input 7:

test.

Sample Output 7:

test

Sample Input 8:

GTA6 никогда не выйдет.

Sample Output 8:

Sample Input 9:

Уголь, уголь, уголь, уголь.

Sample Output 9:

'''

regex = r'\A[A-Za-zа-яА-яёЁ]{4}\b'
