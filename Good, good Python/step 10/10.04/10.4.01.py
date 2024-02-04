'''

Подвиг 5. Пользователь может ввести с клавиатуры следующие команды в виде строки:

top или Top или TOP
bottom или Bottom или BOTTOM
right или Right или RIGHT
left или Left или LEFT

cmd = input() 

С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран сообщение в формате:

Команда <название команды малыми буквами>

Например, при вводе Top, должны на выходе получить:

Команда top

И так для всех четырех команд. Если тип команды не определен, то вывести строку:

Неверная команда
 

Sample Input:

BOTTOM

Sample Output:

Команда bottom

'''

cmd = input()
match cmd:
    case 'top' | 'Top' | 'TOP':
        print(f"Команда {cmd.lower()}")
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print(f"Команда {cmd.lower()}")
    case 'left' | 'Left' | 'LEFT':
        print(f"Команда {cmd.lower()}")
    case 'right' | 'Right' | 'RIGHT':
        print(f"Команда {cmd.lower()}")
    case _:
        print(f"Команда {cmd.lower()}")
