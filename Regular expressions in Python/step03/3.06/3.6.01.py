'''

Найдите все последовательности, используя \w.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из \w
    Длина - максимально возможная

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Все найденные последовательности, каждая на новой строке.

Sample Input 1:

يحتاج الجسم القوي إلى عقل قوي.

Sample Output 1:

يحتاج
الجسم
القوي
إلى
عقل
قوي

Sample Input 2:

Recognition is the most powerful motivation factor.

Sample Output 2:

Recognition
is
the
most
powerful
motivation
factor

Sample Input 3:

Máme otevřeno 24 hodin denně.

Sample Output 3:

Máme
otevřeno
24
hodin
denně

Sample Input 4:

這個理論有一個缺點。

Sample Output 4:

這個理論有一個缺點

Sample Input 5:

Бездә бәхәссез дәлил бар.

Sample Output 5:

Бездә
бәхәссез
дәлил
бар

Sample Input 6:

1234567890_+

Sample Output 6:

1234567890_

'''

import re

result = re.finditer(r'\w+', input(), 0)
for i in result:
    print(i.group())
