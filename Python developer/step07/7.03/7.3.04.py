'''

Дан список чисел, записанных через пробел. Реализуйте кучу с максимумом в вершине для этого списка.

Далее программе на вход будут поступать команды:

    insert <число> – добавить число в кучу;
    pop – удалить вершину и напечатать ее;
    end – завершить выполнение программы.

Ввод:

    nums – список чисел записанных через пробел
    Список команд.

Вывод:

Результаты работы программы

Sample Input:

1 5 2 6 3 7 4 8
insert 20
pop
insert 0
pop
insert 4
pop
end

Sample Output:

20
8
7

'''

from heapq import heappush, heappop

nums = [int(i)*-1 for i in input().split()]
nums.sort()

while True:
    command = input().split()
    match command[0]:
        case 'insert':
            heappush(nums, int(command[1])*-1)
        case 'pop':
            print(heappop(nums)*-1)
        case 'end':
            exit(0)
