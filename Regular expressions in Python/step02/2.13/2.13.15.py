'''

Найдите все валидные пустые массивы, или массивы с числами. Числом считаем произвольную последовательность из цифр.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с [ и заканчиваются на ]
    Внутри может быть пусто, а могут находиться числа
    Числом считаем произвольную последовательность из цифр
    Между числами должны стоять запятые
    Запятые могут быть как и с пробелом, так и без
    После последнего числа может стоять запятая, т.к. такие массивы: [123, 123, ] и [23, ] валидные в Python

Sample Input 1:

[1, 23, 3, 436, 5, 63673, 47][2][][4, 05][1, 2, 3, 4, 5, 6, 7424234234234243242, 5][6246546456][432][0][3240, 00] [402030, 404040]

Sample Output 1:

[1, 23, 3, 436, 5, 63673, 47] [2] [] [4, 05] [1, 2, 3, 4, 5, 6, 7424234234234243242, 5] [6246546456] [432] [0] [3240, 00] [402030, 404040]

Sample Input 2:

[0][10][01]

Sample Output 2:

[0] [10] [01]

Sample Input 3:

[1234, 04] [423423, 582945023, 94235020, 0852] [2525, 0][, 123, 123][, ][,324]

Sample Output 3:

[1234, 04] [423423, 582945023, 94235020, 0852] [2525, 0]

Sample Input 4:

[123, 123, ] [23, ]

Sample Output 4:

[123, 123, ] [23, ]

Sample Input 5:

[1,23,3,436,5,63673,47] [2] [] [1,2, 3,4, 5,6, 7424234234234243242,5] [6246546456] [432] [402030, 404040]

Sample Output 5:

[1,23,3,436,5,63673,47] [2] [] [1,2, 3,4, 5,6, 7424234234234243242,5] [6246546456] [432] [402030, 404040]

Sample Input 6:

[2022 2022][1 2 3 4]

Sample Output 6:

'''

regex = r'(?:\[(\d+\,\s?)(\d+\,?\s?)*\])|\[\d+,?\s?\]|\[\d+,*\s*\]|\[\]'
