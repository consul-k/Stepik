'''

Подвиг 3. Вводятся названия городов в одну строчку через пробел. На основе этой строки необходимо сформировать список из названий. 
А, затем, используя оператор распаковки *, преобразовать этот список в кортеж lst_c. Результат вывести на экран командой:

print(lst_c)

Sample Input:

Москва Уфа Тверь Самара

Sample Output:

('Москва', 'Уфа', 'Тверь', 'Самара')

'''

# put your python code here
string = input().split()
lst_c = (*string,)
print(lst_c)
