'''

Получите все идентификаторы видеороликов на YouTube, используя регулярные выражения.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Cостоит из символов латинского алфавита обоих регистров, цифр, а также _
    Перед последовательностью стоит v=

Sample Input 1:

https://youtu.be/watch?v=dQw4w9WgXcQ&list=PLi9drqWffJ9FWBo7ZVOiaVy0UQQEm4IbP

Sample Output 1:

dQw4w9WgXcQ

Sample Input 2:

https://www.youtube.com/watch?v=jNQXAC9IVRw

Sample Output 2:

jNQXAC9IVRw

Sample Input 3:

https://m.youtube.com/watch?v=pXRviuL6vMY&list=PLrhpb4TQr-uKzxOB1C_9x-Ysrj2WRMZN_&index=16&t=535s

Sample Output 3:

pXRviuL6vMY

Sample Input 4:

https://www.youtube.com/watch?app=desktop&v=WUEVJ0N6I1A&t=1s

Sample Output 4:

WUEVJ0N6I1A

'''

regex = r'(?<=v\=)[a-zA-Z0-9_]+'
