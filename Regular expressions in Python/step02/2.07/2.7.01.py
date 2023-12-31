'''

Напишите регулярное выражение, которое найдёт все последовательности из любых пяти символов, кроме перехода на следующую строку.

Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из 5 символов
    Используются все символы, кроме перехода на новую строку

Sample Input 1:

Этот текст был разделён на последовательности из 5 символов, и каждая последовательность была выведена в консоль через пробел.

Sample Output 1:

Этот  текст  был  разде лён н а пос ледов атель ности  из 5  симв олов,  и ка ждая  после доват ельно сть б ыла в ыведе на в  консо ль че рез п робел

Sample Input 2:

Вам выводить в консоль ничего не нужно, вам нужно написать только само регулярное выражение.

Sample Output 2:

Вам в ыводи ть в  консо ль ни чего  не ну жно,  вам н ужно  напис ать т олько  само  регу лярно е выр ажени

Sample Input 3:

<=>?@ABCDEwxyz{|}~абвгдеёжз

Sample Output 3:

<=>?@ ABCDE wxyz{ |}~аб вгдеё

Sample Input 4:

<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;

Sample Output 4:

<=>?@ ABCDE FGHIJ KLMNO PQRST UVWXY Z[]^_ `abcd efghi jklmn opqrs tuvwx yz{|} ~абвг деёжз ийклм нопрс туфхц чшщъы ьэюяА БВГДЕ ЁЖЗИЙ КЛМНО ПРСТУ ФХЦЧШ ЩЪЫЬЭ ЮЯ !" #$%&\ '()*+ ,-./0 12345 6789:

'''

regex = r'[\S ]{5}'
