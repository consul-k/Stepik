'''

Найдите все пятибуквенные слова в тексте.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из букв латинского и кириллического алфавитов обоих регистров
    Длина - 5 букв
    Не является подпоследовательностью

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Все пятибуквенные слова в полученной строке.

Sample Input 1:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vestibulum ex lectus, ut rutrum lacus sollicitudin in. Maecenas placerat aliquam nisl, id ultricies justo maximus ac. Sed massa ex, feugiat fermentum viverra ultrices, varius at odio. Nunc facilisis viverra vestibulum. Donec nec erat a tortor faucibus consequat et at massa. Proin tincidunt sem at nibh feugiat, id aliquam nulla luctus. Nulla fermentum ultricies orci et egestas. Quisque placerat sem sit amet erat cursus aliquam. Cras malesuada, felis vestibulum volutpat sollicitudin, odio sapien varius sem, sit amet lobortis neque lectus imperdiet erat. Proin ac ex nec felis sodales mattis. Quisque ultrices varius lectus ut convallis. Donec dui nunc, pellentesque varius tortor sed, feugiat tincidunt lorem.

Sample Output 1:

Lorem
ipsum
dolor
lacus
justo
massa
Donec
massa
Proin
nulla
Nulla
felis
neque
Proin
felis
Donec
lorem

Sample Input 2:

Мы вынуждены отталкиваться от того, что разбавленное изрядной долей эмпатии, рациональное мышление способствует подготовке и реализации модели развития. В целом, конечно, консультация с широким активом предоставляет широкие возможности для форм воздействия.

Sample Output 2:

долей
целом

Sample Input 3:

Актёр

Sample Output 3:

Актёр

'''

import re

result = re.finditer(r'\b[a-zA-Zа-яА-ЯёЁ]{5}\b', input(), 0)
for i in result:
    print(i.group())
