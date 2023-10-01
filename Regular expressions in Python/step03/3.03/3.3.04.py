'''

Даны данные в формате JSON. С помощью регулярных выражений нужно получить ключ t и его значение.
Что нужно сделать:

 Нужно найти ключ t и его значение:

    Значением является последовательностью из арабских цифр, символов . и +
    Перед значением стоит t=

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка с данными в формате JSON.
Выходные данные:

Выведите в консоль ключ t и его значение.

Sample Input 1:

{"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below","errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.555555+11232131"}

Sample Output 1:

t=0.555555+11232131

Sample Input 2:

{"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below","errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.5553455+184231"}

Sample Output 2:

t=0.5553455+184231

Sample Input 3:

{"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below","errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.4234253455+1543553431"}

Sample Output 3:

t=0.4234253455+1543553431

'''

import re

result = re.search(r't=[0-9\.\+]+', input())
if result:
    print(result.group())
