'''

Напишите программу, которая будет эмулировать функциональность стека. Вам на вход будут поступать четыре команды:

    add <число> – добавить в стек число
    pop – удалить из стека число и напечатать его
    head – вывести текущий элемент стека
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

10
10
9
7
5

'''

stack = []

while True:
    command = input().split()
    match command[0]:
        case 'add':
            stack.append(command[1])
        case 'pop':
            print(stack.pop())
        case 'head':
            print(stack[-1])
        case 'close':
            exit(0)
