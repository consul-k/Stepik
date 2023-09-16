'''

Напишите регулярное выражение, которое найдёт все числа, написанные с помощью римских цифр.

Что нужно найти:

Нужно найти последовательности, состоящие из римских цифр: IVXLCDM.

Sample Input 1:

В MMXIII году в школе CXXIII состоялся очередной выпуск XI классов.

Sample Output 1:

MMXIII CXXIII XI

Sample Input 2:

Эх, как же хорошо было в XIX веке.

Sample Output 2:

XIX

Sample Input 3:

Сейчас MMXXII год.

Sample Output 3:

MMXXII

Sample Input 4:

Людовик XVIII

Sample Output 4:

XVIII

'''

regex = r'\b[IVXLCDM]+\b'
