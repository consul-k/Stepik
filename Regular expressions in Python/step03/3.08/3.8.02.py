'''

Разделите текст на слова.
Что нужно сделать:

Нужно разделить текст на слова по следующим символам: .?!, .
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Список после разделения текста на слова.

Sample Input 1:

Привет, как твои дела? Привет, нормально, учу регулярные выражения.

Sample Output 1:

['Привет', '', 'как', 'твои', 'дела', '', 'Привет', '', 'нормально', '', 'учу', 'регулярные', 'выражения', '']

Sample Input 2:

The first one is heavy!This actually goes really well with Chris's workout he's doing.

Sample Output 2:

['The', 'first', 'one', 'is', 'heavy', 'This', 'actually', 'goes', 'really', 'well', 'with', "Chris's", 'workout', "he's", 'doing', '']

'''

import re

result = re.split(r'[.?!, ]', input())
print(result)
