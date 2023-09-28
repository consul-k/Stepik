'''

Найдите в тексте все названия файлов и их расширения.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Название файла состоит из: букв латинского алфавита верхнего и нижнего регистров, цифр, -
    Между названием и расширением файла стоит .
    Расширение файла состоит из букв латинского алфавита верхнего и нижнего регистров, цифр
    Минимальная длина названия и расширения - один символ
    Найденная последовательность может являться подпоследовательностью, только если стоит в абсолютном или относительном пути: C:\Users\test.txt, ../Users/test.txt, т.е. перед ней стоят символы / или \

Sample Input 1:

Untitled-1.psd Untitled-1.jpg video.mp4

Sample Output 1:

Untitled-1.psd Untitled-1.jpg video.mp4

Sample Input 2:

C:\Users\matv3\Desktop\script.js index.html @/assets/images/logo.svg

Sample Output 2:

script.js index.html logo.svg

Sample Input 3:

bot.py sad.gif

Sample Output 3:

bot.py sad.gif

Sample Input 4:

.mp4 some-text .py

Sample Output 4:

Sample Input 5:

test... te..st

Sample Output 5:

Sample Input 6:

файл.file файл.файл file.файл фfile.фfile fфile.fфile

Sample Output 6:

Sample Input 7:

c#logs.txt query.$exe

Sample Output 7:

Sample Input 8:

 :a.json  ?s.csv

Sample Output 8:

'''

regex = r'\b(?<![\w#@$&%?:;,])[a-zA-Z0-9-]+\.[a-zA-Z0-9]+\b|(?=[\\\/])[a-zA-Z0-9-]+\.[a-zA-Z0-9]+'
