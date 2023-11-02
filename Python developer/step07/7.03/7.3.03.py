'''

Напишите программу, которая будет эмулировать функциональность очереди. Вам на вход будут поступать три команды:

    add <число> – добавить в очередь число
    pop – удалить из очереди число и напечатать его
    head – вывести текущий элемент очереди
    close – завершить программу

Ввод:

Список комманд

Вывод:

Ответы на команды 

Sample Input:

add 5
add 10
head
pop
add 7
add 9
pop
pop
head
close

Sample Output:

5
5
10
7
9

'''

from collections import deque

queue = deque()

while True:
    command = input().split()
    match command[0]:
        case 'add':
            queue.appendleft(command[1])
        case 'pop':
            print(queue.pop())
        case 'head':
            print(queue[-1])
        case 'close':
            exit(0)
