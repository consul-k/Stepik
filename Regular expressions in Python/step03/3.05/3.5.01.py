'''

Дарья ждёт милого мальчика, который напишет ей ночью: номер, срок действия, владельца, CVV. Помогите ей проверить номер банковской карты.
Что нужно сделать:

Найдите все последовательности цифр, которые начинаются от 13 цифр включительно.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если это номер карты - выводите True, иначе - False.

Sample Input 1:

1234567891011121

Sample Output 1:

True

Sample Input 2:

8910111213457

Sample Output 2:

True

Sample Input 3:

1234567891011121314

Sample Output 3:

True

Sample Input 4:

890111213457

Sample Output 4:

False

Sample Input 5:

4235sfd53433

Sample Output 5:

False

'''

import re

result = re.fullmatch('\d{13,}', input())
print(bool(result))
