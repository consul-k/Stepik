'''

Подвиг 1. На вход программы поступает список наименований рек, записанных в одну строчку через пробел. 
Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.

Sample Input:

Лена Енисей Волга Дон

Sample Output:

Енисей Волга Лена Дон

'''

# put your python code here
print(*sorted(input().split(), key=len, reverse=True))
