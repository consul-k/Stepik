'''

Подвиг 4. Вводится список названий городов в одну строчку через пробел. Выберите из этого списка один город случайным образом и отобразите его на экране.

Sample Input:

Тула Казань Смоленск Семипалатинск Уфа Москва Самара

Sample Output:

Казань

'''

import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
s = input().split()
print(random.choice(s))
