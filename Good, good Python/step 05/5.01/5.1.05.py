'''

Подвиг 6. Вводится строка (слаг). Замените в этой строке все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-). 
Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.

Sample Input:

osnovnye--metody-----slovarey

Sample Output:

osnovnye-metody-slovarey

'''

import re

string = input()
result = re.sub(r"-+", "-", string)
print(result)
