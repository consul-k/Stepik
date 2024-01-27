'''

Подвиг 6. В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, 
переданного ей итерируемого объекта и возвращает сформированный кортеж значений.

На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Вызовите функцию filter_lst для формирования:

- кортежа из всех значений входного списка (передается в параметр it);
- кортежа только из отрицательных чисел;
- кортежа только из неотрицательных чисел (то есть, включая и 0);
- кортежа из чисел в диапазоне [3; 5]

Каждый результат работы функции следует отображать с новой строки командой:

print(*lst)

где lst - список на возвращенный функцией filter_lst. 
Для отбора нужных значений формальному параметру key следует передавать соответствующие определения анонимной функции.
 

Sample Input:

5 4 -3 4 5 -24 -6 9 0

Sample Output:

5 4 -3 4 5 -24 -6 9 0
-3 -24 -6
5 4 4 5 9 0
5 4 4 5

'''

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)
    res = ()
    for x in it:
        if key(x):
            res += (x,)
    return res
sp = input().split()
print(*filter_lst(sp)) 
print(*filter_lst(sp, lambda x: int(x)<0))
print(*filter_lst(sp, lambda x: int(x)>=0))
print(*filter_lst(sp, lambda x: 3<=int(x)<=5))
