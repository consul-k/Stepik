'''

Давайте напишем простого бота-счетовода, которому на вход поступают несколько команд, а он выполняет вычисления. 
У бота есть внутренний счетчик, который изначально равен 0, который он использует.

    zero – обнуляет число
    add <number> – добавляет к числу number
    minus <number> – отнимает число number
    mul <number> – умножает на число number
    div <number> – делит число нацело на number 
    result – выводит промежуточный результат
    exit – завершает выполнение программы

number – всегда целое число!

Ввод:

Список команд, который завершается командой exit.

Вывод:

Все промежуточные выводы программы

Sample Input 1:

add 5
mul 5
result
exit

Sample Output 1:

25

Sample Input 2:

result
exit

Sample Output 2:

0

Sample Input 3:

exit

Sample Output 3:

Sample Input 4:

add 2
result
mul 3
result
minus 4
result
div 2
result
zero
result
exit

Sample Output 4:

2
6
2
1
0

'''

number = 0
while True:
    command = input().split()
    match command[0]:
        case "add":
            number += int(command[1])
        case "minus":
            number -= int(command[1])
        case "mul":
            number *= int(command[1])
        case "div":
            number //= int(command[1])
        case "result":
            print(number)
        case "zero":
            number = 0
        case "exit":
            exit(0)
print(number)
