'''

Очень часто номера телефонов вводят по-разному. Иногда ставят скобки, иногда тире, иногда пробелы, иногда вообще ничего не ставят. 
Напишите регулярное выражение, которое найдёт все такие номера.

Что нужно сделать:

Найдите все последовательности, которые могут быть номерами телефонов:

    Номер может начинаться с +
    Потом идут цифры
    В каждом номере минимум 11 цифр
    Между цифрами могут быть разделители: ( )-
    Длина разделителя от 0 до 2 символов включительно

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если это номер телефона - выводите True, иначе - False.

Sample Input 1:

7(977)8179710

Sample Output 1:

True

Sample Input 2:

+79786655917

Sample Output 2:

True

Sample Input 3:

89175643308

Sample Output 3:

True

Sample Input 4:

+7 902 7993132

Sample Output 4:

True

Sample Input 5:

8 (922) 007-62-31

Sample Output 5:

True

Sample Input 6:

8 983 353 12 49

Sample Output 6:

True

Sample Input 7:

+7 909 789-33-08

Sample Output 7:

True

Sample Input 8:

19362136208

Sample Output 8:

True

Sample Input 9:

+688 893 512 92 14

Sample Output 9:

True

Sample Input 10:

7[977]8179710

Sample Output 10:

False

Sample Input 11:

7(977)817_97_10

Sample Output 11:

False

Sample Input 12:

+777866559

Sample Output 12:

False

Sample Input 13:

+7 702 79938

Sample Output 13:

False

Sample Input 14:

8 (722) -007-62-31

Sample Output 14:

False

Sample Input 15:

-8 (783 35312 49

Sample Output 15:

False

Sample Input 16:

7 809 789f33-08

Sample Output 16:

False

Sample Input 17:

7 942 674 85 5

Sample Output 17:

False

'''

import re

result = re.fullmatch('\+?(\d[() -]{0,2}){11,}', input())
print(bool(result))
