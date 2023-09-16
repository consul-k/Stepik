'''

Напишите регулярное выражение, которое извлекает протокол полученной ссылки: http или https. Если протокола нет - ничего искать не надо.

Что нужно найти:

Протокол http или https, у которого есть граница справа

Sample Input 1:

https://regex101.com/

Sample Output 1:

https

Sample Input 2:

http://127.0.0.1:5500/index.html

Sample Output 2:

http

Sample Input 3:

www.youtube.com

Sample Output 3:

Sample Input 4:

https://stepik.org/course/107335/ http://stepik.org/course/107335/

Sample Output 4:

https http

Sample Input 5:

https://httpsssssssssssss.com/ggtps/hhttps/

Sample Output 5:

https

Sample Input 6:

hhhh://example.com httpp://example.com¶

Sample Output 6:

'''

regex = r'\bhttps{0,1}\b'
