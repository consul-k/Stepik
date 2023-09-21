'''

Напишите регулярное выражение, которое найдёт все последовательности x с чётной длиной.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из символов x
    Длина последовательности чётная
    Последовательность не может быть подпоследовательностью

Sample Input 1:

x xx xxx xxxx xxxxx xxxxxx xxxxxxx xxxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxx

Sample Output 1:

xx xxxx xxxxxx xxxxxxxx xxxxxxxxxx xxxxxxxxxxxx

Sample Input 2:

xxxxxxxxxx xxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxx xxxxxxxxxxxxxx xxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxx

Sample Output 2:

xxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxx

'''

regex = r'\b(?:xx)+\b'
