'''

Напишите регулярное выражение, которое найдёт все последовательности Привет и привет в тексте.

Что нужно найти:

Последовательности: Привет и привет

Sample Input 1:

Привет.

Sample Output 1:

Привет

Sample Input 2:

Do not say 'привет', instead say 'hi'.

Sample Output 2:

привет

Sample Input 3:

Привет-привет

Sample Output 3:

Привет привет

'''

regex = r'[Пп]ривет'
