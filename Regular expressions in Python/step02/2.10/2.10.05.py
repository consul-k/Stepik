'''

Напишите регулярное выражение, которое найдёт все последовательности if и <if>, но не <if и if>, стоящие между началом и концом строки.
Что нужно найти:

    Последовательности if без скобок или со скобками, стоящими с двух сторон: if и <if>
    Последовательность стоит в начале строки
    После последовательности строка заканчивается

Sample Input 1:

<if>

Sample Output 1:

<if>

Sample Input 2:

if

Sample Output 2:

if

Sample Input 3:

<if

Sample Output 3:

Sample Input 4:

if>

Sample Output 4:

Sample Input 5:

if>if><if<><>>if<

Sample Output 5:

'''

regex = r"^(<)?(?(1)(if>)|(if))$"
