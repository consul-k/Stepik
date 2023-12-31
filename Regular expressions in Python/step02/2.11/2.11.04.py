'''

Напишите регулярное выражение, которое найдёт все имена и названия в тексте.

Слова в начале предложения не считаются, так как невозможно проверить это имя или просто слово с заглавной буквы.

Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Последовательность букв, которая начинается на заглавную букву
    Используется кириллический алфавит нижнего и верхнего регистров
    Последовательность не стоит в начале предложения
    Перед последовательностью не должно заканчиваться предложение, т.е. не стоит: .!?

Sample Input 1:

Меня зовут Егор. Мне нравится ходить у реки Волги, что проходит через город Ярославль. Надеюсь, что моя мечта - поездка во Владивосток, скоро осуществится.

Sample Output 1:

Егор Волги Ярославль Владивосток

Sample Input 2:

Владимир знает, что если в этом задании имя в начале предложения - мы должны его пропустить, так как это может быть любое другое слово, которое начинается с большой буквы.

Sample Output 2:

Sample Input 3:

Неправильно ты, дядя Фёдор, бутерброд ешь.

Sample Output 3:

Фёдор

'''

regex = r'(?<!\A)(?<!(\. ))[А-Я]{1}[а-яё]+\b'
