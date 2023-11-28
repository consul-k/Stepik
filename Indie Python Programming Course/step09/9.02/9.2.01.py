'''

Напишите функцию find_lines_len_more_6, которая принимает имя файла и находит количество строк, превышающее 6 символов. 
Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.

Функция find_lines_len_more_6 должна возвращать найденное количество строк

Ваша задача написать только определение функции find_lines_len_more_6

'''

def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, 'r') as f:
        cnt = 0
        for line in f:
            if len(x:=line.replace('\n',''))>6:
                cnt+=1
    return cnt
