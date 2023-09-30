'''

Многие функции возвращают None в результате своей работы, если ничего не было найдено.

Попробуйте вывести нулевую группу в Match-объекте, если совпадение было найдено. Если его нет - ничего не выводите.

Sample Input 1:

123
123123

Sample Output 1:

123

Sample Input 2:

123
456789

Sample Output 2:

'''

import re

match = re.match(input(), input())

if match:
    print(match.group())
