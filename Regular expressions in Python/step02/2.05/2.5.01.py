'''

Напишите регулярное выражение, которое найдёт все последовательности тест в тексте.

Что нужно найти:

Все последовательности тест

Пример решения:

regex = r'Тут ваше регулярное выражение'

Sample Input 1:

Предлагаю протестировать влияние слова тест в тестовых данных на результаты работы тестируемой программы.

Sample Output 1:

тест тест тест тест

Sample Input 2:

Тут нету этого слова

Sample Output 2:

Sample Input 3:

Снова тестик

Sample Output 3:

тест

'''

regex = r'тест'
