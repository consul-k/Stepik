'''

Подвиг 5. Объявите функцию с именем create_global, которая имеет, следующую сигнатуру:

def create_global(x): ...

Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x. 
(Ничего выводить на экран она не должна, только создавать переменную).

Вызывать функцию не нужно, только определить.

'''

def create_global(x):
    global TOTAL
    TOTAL = x
